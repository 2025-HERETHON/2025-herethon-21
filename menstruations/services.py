from typing import Optional, TypedDict
from calendar import monthrange
from datetime import date, timedelta
from statistics import mean
from django.db.models import Avg
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from utils.validators import validate_form, validate_auth, validate_permission, validate_unique
from .models import Menstruation
from .forms import MenstruationForm

class PhaseType(TypedDict):
    start: date
    end: date

class MenstruationService:
    DEFAULT_DURATION = 5
    DEFAULT_CYCLE = 28
    MIN_CYCLE = 15
    MAX_CYCLE = 45
    RECENT_COUNT = 6

    def __init__(self, request:HttpRequest, pk:Optional[int]=None):
        instance = get_object_or_404(Menstruation, pk=pk) if pk else None
        self.request = request
        self.instance = instance
        self.form = MenstruationForm(request.POST, instance=instance)

    def _predict_next_menstruation(self):
        menstruations = self.get_list()

        recent_menstruation_list = list(menstruations[:self.RECENT_COUNT])
        recent_duration_list = [menstruation.duration for menstruation in recent_menstruation_list]
        recent_cycle_list = [menstruation.cycle for menstruation in recent_menstruation_list if self.MIN_CYCLE <= menstruation.cycle <= self.MAX_CYCLE]

        last_menstruation_start = menstruations.first().start # 회원가입 시 월경을 필수로 입력하므로 레코드가 1개 이상임을 보장함.
        avg_duration = mean(recent_duration_list) if recent_duration_list else self.DEFAULT_DURATION
        avg_cycle = mean(recent_cycle_list) if recent_cycle_list else self.DEFAULT_CYCLE

        next_start = last_menstruation_start + timedelta(days=avg_cycle)
        next_end = next_start + timedelta(days=avg_duration-1)
        next_menstruation = { 'start': next_start, 'end': next_end, 'cycle': avg_cycle }

        menstruation_list = [
            {
                'start': menstruation.start,
                'end': menstruation.end,
                'cycle': menstruation.cycle,
            }
            for menstruation in menstruations
        ]
        
        return next_menstruation, menstruation_list

    def _calc_cycle_phase(self, menstruation) -> dict[str,PhaseType]:
        follicular_phase:PhaseType = {
            'start': menstruation['start'],
            'end': menstruation['start'] + timedelta(days=(menstruation['cycle']/2)-1)
        }
        ovulatory_phase:PhaseType = {
            'start': follicular_phase['end'] + timedelta(days=1),
            'end': follicular_phase['end'] + timedelta(days=1),
        }
        luteal_phase:PhaseType = {
            'start': ovulatory_phase['end'] + timedelta(days=1),
            'end': ovulatory_phase['end'] + timedelta(days=(menstruation['cycle']/2)-1)
        }
        return {
            'menstrual_phase': {
                'start': menstruation['start'],
                'end': menstruation['end']
            },
            'follicular_phase': follicular_phase,
            'ovulatory_phase': ovulatory_phase,
            'luteal_phase': luteal_phase
        }
    
    def _calc_overlap_days(self, first_date:date, last_date:date, phase_list:list[PhaseType]) -> list[str]:
        overlap_days = set()
        for phase in phase_list:
            overlap_start = max(phase['start'], first_date)
            overlap_end = min(phase['end'], last_date)
            for i in range((overlap_end - overlap_start).days + 1):
                overlap_days.add((overlap_start + timedelta(days=i)).isoformat())
        return sorted(overlap_days)

    @validate_auth
    def get_list(self):
        menstruations = Menstruation.objects.filter(
            user=self.request.user,
        ).defer(
            'created_at','updated_at','user',
        )
        return menstruations

    @validate_auth
    def get_average(self):
        menstruations = self.get_list()
        average_duration = menstruations.aggregate(duration=Avg('duration'))['duration']
        average_cycle = mean([menstruation.cycle for menstruation in menstruations])

        return {
            'duration': round(average_duration, 1) if average_duration else None,
            'cycle': round(average_cycle, 1) if average_cycle else None
        }

    @validate_auth
    def get_cycle(self):
        month_str = self.request.GET.get('month')
        if month_str != None:
            year, month = map(int, month_str.split('-'))
        else:
            now = timezone.now()
            year = now.year
            month = now.month
        first_date = date(year, month, 1)
        last_date = date(year, month, monthrange(year, month)[1])

        next_menstruation, menstruation_list = self._predict_next_menstruation()
        menstruation_list[0]['cycle'] = (menstruation_list[0]['start'] - next_menstruation['start']).days*-1
        menstruation_list.append(next_menstruation)

        target_menstruation_list = [
            menstruation
            for menstruation in menstruation_list
            if (menstruation['start'] <= last_date) and (menstruation['end'] >= first_date)
        ]

        phase_list = [self._calc_cycle_phase(menstruation) for menstruation in target_menstruation_list]

        return {
            'menstrual_phase': self._calc_overlap_days(first_date, last_date, [phase['menstrual_phase'] for phase in phase_list]),
            'follicular_phase': self._calc_overlap_days(first_date, last_date, [phase['follicular_phase'] for phase in phase_list]),
            'ovulatory_phase': self._calc_overlap_days(first_date, last_date, [phase['ovulatory_phase'] for phase in phase_list]),
            'luteal_phase': self._calc_overlap_days(first_date, last_date, [phase['luteal_phase'] for phase in phase_list])
        }

    @validate_unique
    @validate_form
    @validate_auth
    def post(self):
        created_menstruation:Menstruation = self.form.save(commit=False)
        created_menstruation.user = self.request.user
        created_menstruation.duration = (created_menstruation.end - created_menstruation.start).days + 1
        created_menstruation.save()
        return '월경을 추가했습니다.'

    @validate_unique
    @validate_form
    @validate_permission
    @validate_auth
    def put(self):
        updated_menstruation:Menstruation = self.form.save(commit=False)
        updated_menstruation.duration = (updated_menstruation.end - updated_menstruation.start).days + 1
        updated_menstruation.save()
        return '월경을 수정했습니다.'

    @validate_permission
    @validate_auth
    def delete(self):
        self.instance.delete()
        return '월경을 삭제했습니다.'