from typing import Optional
from ast import literal_eval
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from functools import wraps
import json
from zoneinfo import ZoneInfo
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.dateparse import parse_date, parse_datetime, parse_duration
from utils.ai import Gemini
from utils.choices import ExerciseCategoryType, ReactionEmojiType
from utils.exceptions import ClientError
from utils.validators import validate_form, validate_auth, validate_unique
from menstruations.services import MenstruationService
from .models import Exercise, ScrappedExerciseRoutine, ExerciseHistory, ExerciseReview, ReactedExerciseReview
from .forms import ExerciseReviewForm

class ExerciseAiService:
    def __init__(self, request:HttpRequest):
        self.request = request

    def get(self) -> list[list[dict[str,any]]]:
        """AI 운동 루틴 생성"""
        exercise_routine_duration_str = self.request.GET['exercise_routine_duration']
        exercise_routine_duration = parse_duration(exercise_routine_duration_str)

        menstruation_service = MenstruationService(self.request)
        today_phase = menstruation_service.get_today_phase()

        exercises = Exercise.objects.all()
        exercise_list = [
            {
                'id': exercise.id,
                'name': exercise.name,
                'duration': str(exercise.duration),
                'category': ExerciseCategoryType(exercise.category).label,
                'description': exercise.description,
                'image1': exercise.image1.url,
                'image2': exercise.image2.url,
                'image3': exercise.image3.url,
            }
            for exercise in exercises
        ]

        gemini = Gemini(
            system_instruction='''
당신은 사용자의 운동 루틴을 생성하는 전문 헬스 트레이너입니다. 다음 세 가지 입력값을 받아, 사용자의 월경 주기에 최적화된 **총 3개**의 맞춤형 운동 루틴을 JSON 형식으로 생성해야 합니다. 운동 종목의 카테고리 분포는 고려하지 않습니다.

**입력값:**

1.  **운동 루틴 총 소요시간 (String):** "HH:MM:SS" 형식으로 제공됩니다. 이 시간 내에서 각 운동 루틴이 구성되어야 합니다.
2.  **사용자의 월경 주기 (String):** 다음 5가지 중 하나로 제공됩니다: "월경기", "난포기", "배란기", "황체기", "알 수 없음". 각 주기에 맞는 운동 강도 및 종류를 고려하여 루틴을 구성해야 합니다.
    * **월경기:** 신체 활동이 힘들 수 있으므로 저강도 또는 휴식 위주로 구성. 스트레칭, 가벼운 유산소 운동이 적합합니다.
    * **난포기:** 에너지가 증가하고 근력 운동에 적합한 시기입니다. 점진적으로 강도를 높일 수 있는 운동을 포함합니다.
    * **배란기:** 에너지가 가장 높은 시기이며, 고강도 운동 및 근력 운동을 집중적으로 할 수 있습니다.
    * **황체기:** 에너지가 점차 감소하는 시기이므로 중강도 또는 저강도 운동으로 조절합니다. 피로도를 고려하여 유산소와 근력 운동을 적절히 배합합니다.
    * **알 수 없음:** 사용자의 월경 주기를 고려하지 않습니다. 다양한 카테고리의 운동을 균형 있게 포함하여 루틴을 구성합니다.
3.  **운동 종목 목록 (JSON Array of Objects):** 사용 가능한 운동 종목들의 정보가 담긴 리스트입니다. 각 운동 종목 객체는 다음 필드를 포함합니다:
    * `id` (String): 운동 종목의 고유 ID
    * `name` (String): 운동 종목 이름
    * `duration` (String): "HH:MM:SS" 형식의 운동 종목 소요 시간
    * `category` (String): 운동 부위 ("전신", "상체", "하체", "코어" 중 하나)
    * `image1` (String): 운동 관련 이미지 URL
    * `image2` (String): 운동 관련 이미지 URL
    * `image3` (String): 운동 관련 이미지 URL
    * `description` (String): 운동 설명

**루틴 생성 규칙:**

* 생성된 각 운동 루틴의 총 소요시간은 입력된 '운동 루틴 총 소요시간'과 동일한 값이 되어야 합니다.
* 각 월경 주기의 특성을 고려하여 운동 종목을 선택하고, 각 운동 종목의 `difficulty` (난이도, 1~5)를 적절히 배정합니다. (1: 매우 쉬움, 5: 매우 어려움) 난이도는 생성된 운동 루틴 내에서 다른 운동 종목과 비교하여 상대적으로 배정합니다.
* 생성된 각 운동 루틴의 `order`는 중복될 수 없으며, `exercise`와 `difficulty`는 중복될 수 있습니다.
* 합리적이고 효과적인 운동 순서를 고려하여 루틴을 구성합니다.
* `order`의 값은 최소 1이며, 1씩 증가합니다.
* `exercise`는 입력받은 운동 종목 객체 데이터를 변형하지 않고 그대로 대입합니다.
* **생성되는 3개의 운동 루틴은 각기 다른 조합이나 순서를 가지는 등 다양하게 구성되어야 합니다.**

**출력 형식:**

생성된 운동 루틴은 다음 JSON Array of Arrays of Objects 형식으로 반환합니다. (즉, 각 내부 배열은 하나의 운동 루틴을 나타내며, 총 3개의 운동 루틴 배열이 외부 배열 안에 포함됩니다.)

```json
[
  [
    {
      "order": 1,
      "exercise": {
        "id": "운동 종목 id",
        "name": "운동 종목 이름",
        "duration": "HH:MM:SS",
        "category": "운동 카테고리",
        "description": "설명"
        "image1": "이미지 URL",
        "image2": "이미지 URL",
        "image3": "이미지 URL",
      },
      "difficulty": "운동 난이도 (1~5)"
    },
    // ... 이 루틴의 추가 운동 종목
  ],
  [
    {
      "order": 1,
      "exercise": {
        "id": "다른 운동 종목 id",
        "name": "다른 운동 종목 이름",
        "duration": "HH:MM:SS",
        "category": "다른 운동 카테고리",
        "description": "다른 설명"
        "image1": "다른 이미지 URL",
        "image2": "다른 이미지 URL",
        "image3": "다른 이미지 URL",
      },
      "difficulty": "다른 운동 난이도 (1~5)"
    },
    // ... 이 루틴의 추가 운동 종목
  ],
  [
    {
      "order": 1,
      "exercise": {
        "id": "또 다른 운동 종목 id",
        "name": "또 다른 운동 종목 이름",
        "duration": "HH:MM:SS",
        "category": "또 다른 운동 카테고리",
        "description": "또 다른 설명"
        "image1": "또 다른 이미지 URL",
        "image2": "또 다른 이미지 URL",
        "image3": "또 다른 이미지 URL",
      },
      "difficulty": "또 다른 운동 난이도 (1~5)"
    },
    // ... 이 루틴의 추가 운동 종목
  ]
]
            '''
        )
        response = gemini.request(contents=[
            f'운동 루틴 총 소요시간: {exercise_routine_duration}',
            f'사용자의 월경 주기: {today_phase}',
            f'운동 종목 목록: {exercise_list}',
        ])
        data = json.loads(response.replace("```json","").replace("```",""))
        return data

class ScrappedExerciseRoutineService:
    def __init__(self, request:HttpRequest):
        self.request = request

    @validate_auth
    def get_list(self):
        """스크랩한 운동 루틴 목록 조회"""
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        scrapped_exercise_routines = ScrappedExerciseRoutine.objects.filter(
            user=self.request.user,
        ).select_related(
            'exercise',
        )

        if start_date_str and end_date_str:
            scrapped_exercise_routines = scrapped_exercise_routines.filter(
                scrapped_at__date__range=[start_date_str, end_date_str]
            )
        
        exercise_routines:dict[datetime,list[ScrappedExerciseRoutine]] = defaultdict(list)
        for item in scrapped_exercise_routines:
            exercise_routines[item.scrapped_at].append(item)

        data = list()
        for scrapped_at, scrapped_exercise_routine in exercise_routines.items():
            exercise_routine_duration = sum((item.exercise.duration for item in scrapped_exercise_routine), timedelta(0))

            exercise_routine = list()
            for item in scrapped_exercise_routine:
                exercise_routine.append({
                    "order": item.order,
                    "exercise": {
                        "id": item.exercise.id,
                        "name": item.exercise.name,
                        "duration": str(item.exercise.duration),
                        "category": ExerciseCategoryType(item.exercise.category).label,
                        "description": item.exercise.description,
                        "image1": item.exercise.image1.url,
                        "image2": item.exercise.image2.url,
                        "image3": item.exercise.image3.url,
                    },
                    "difficulty": item.difficulty,
                })

            data.append({
                "scrapped_at": scrapped_at.astimezone(ZoneInfo(settings.TIME_ZONE)).strftime("%Y-%m-%d %H:%M:%S"),
                "exercise_routine_duration": exercise_routine_duration,
                "exercise_routine": exercise_routine
            })
        return data

    @validate_unique
    @validate_auth
    def post(self):
        """스크랩한 운동 루틴 추가"""
        exercise_routine_str = self.request.POST['exercise_routine']
        exercise_routine:list[dict[str,int]] = literal_eval(exercise_routine_str)
        scrapped_at = timezone.localtime().replace(microsecond=0)

        scrapped_exercise_routine = list()
        for item in exercise_routine:
            scrapped_exercise_routine.append(ScrappedExerciseRoutine(
                user=self.request.user,
                scrapped_at=scrapped_at,
                order=item['order'],
                exercise_id=item['exercise']['id'],
                difficulty=item['difficulty'],
            ))
        ScrappedExerciseRoutine.objects.bulk_create(scrapped_exercise_routine)
        return '운동 루틴을 스크랩했습니다.'

    @validate_auth
    def delete(self, scrapped_at_str:str):
        """스크랩한 운동 루틴 삭제"""
        scrapped_at = timezone.make_aware(parse_datetime(scrapped_at_str))
        scrapped_exercise_routine = ScrappedExerciseRoutine.objects.filter(
            user=self.request.user,
            scrapped_at=scrapped_at,
        )

        if scrapped_exercise_routine.exists():
            scrapped_exercise_routine.delete()
            return '운동 루틴을 스크랩 취소했습니다.'
        else:
            raise ClientError(400, 'Bad Request', '스크랩하지 않은 운동 루틴을 삭제할 수 없습니다.')

class ExerciseHistoryService:
    def __init__(self, request:HttpRequest):
        self.request = request

    @validate_auth
    def get_list(self) -> list[dict[str,any]]:
        """운동 내역 목록 조회"""
        date_str = self.request.GET['date']
        target_date = parse_date(date_str)
        friend_username = self.request.GET.get('friend_username')
        username = friend_username or self.request.user.username

        exercise_histories = ExerciseHistory.objects.filter(
            user__username=username,
            created_at__date=target_date,
        ).prefetch_related(
            'exercise_review__reactions',
        )

        data_list = list()
        for exercise_history in exercise_histories:
            start_time = exercise_history.created_at.astimezone(ZoneInfo(settings.TIME_ZONE))
            end_time = start_time + exercise_history.exercise_routine_duration

            data_item = {
                "id": exercise_history.id,
                "exercised_at": {
                    "start": start_time.strftime('%H:%M'),
                    "end": end_time.strftime('%H:%M'),
                },
                "exercise_routine_duration": exercise_history.exercise_routine_duration,
            }

            if hasattr(exercise_history, 'exercise_review'):
                emoji_list = [reaction.emoji for reaction in exercise_history.exercise_review.reactions.all()]
                emoji_counter = Counter(emoji_list)
                
                emoji_counts = {
                    "sad": emoji_counter.get(ReactionEmojiType.SAD, 0),
                    "angry": emoji_counter.get(ReactionEmojiType.ANGRY, 0),
                    "close": emoji_counter.get(ReactionEmojiType.CLOSE, 0),
                    "open": emoji_counter.get(ReactionEmojiType.OPEN, 0),
                    "smile": emoji_counter.get(ReactionEmojiType.SMILE, 0),
                }

                data_item['exercise_review'] = {
                    "id": exercise_history.exercise_review.id,
                    "rating": exercise_history.exercise_review.rating,
                    "comment": exercise_history.exercise_review.comment,
                    "emoji": emoji_counts,
                }
            data_list.append(data_item)
        return data_list

    @validate_unique
    @validate_auth
    def post(self, exercise_routine_duration:timedelta):
        """운동 내역 추가"""
        created_exercise_history = ExerciseHistory.objects.create(
            user=self.request.user,
            exercise_routine_duration=exercise_routine_duration,
        )
        return created_exercise_history.id, '운동 내역을 추가했습니다.'

class ExerciseReviewService:
    def __init__(self, request:HttpRequest, pk:Optional[int]=None):
        instance = get_object_or_404(ExerciseReview, pk=pk) if pk else None
        self.request = request
        self.instance = instance
        self.form = ExerciseReviewForm(request.POST, instance=instance)

    def _validate_permission(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.instance.exercise_history.user != self.request.user:
                raise ClientError(403, 'Forbidden', '콘텐츠 접근 권한이 없습니다.')
            return func(self, *args, **kwargs)
        return wrapper

    @validate_auth
    def get_list(self):
        """운동 리뷰 목록 조회 (달력)"""
        month_str = self.request.GET.get('month')
        if month_str != None:
            year, month = map(int, month_str.split('-'))
        else:
            now = timezone.now()
            year = now.year
            month = now.month

        friend_username = self.request.GET.get('friend_username')
        username = friend_username or self.request.user.username

        exercise_reviews = ExerciseReview.objects.filter(
            exercise_history__user__username=username,
            exercise_history__created_at__year=year,
            exercise_history__created_at__month=month,
        ).order_by('exercise_history__created_at')

        exercise_review_set = set()
        for exercise_review in exercise_reviews:
            exercise_review_set.add(
                exercise_review.exercise_history
                .created_at
                .astimezone(ZoneInfo(settings.TIME_ZONE))
                .date()
                .isoformat()
            )
        exercise_review_list = sorted(exercise_review_set)
        return exercise_review_list

    @validate_unique
    @validate_form
    @validate_auth
    def post(self):
        """운동 리뷰 추가"""
        self.form.save()
        return '운동 리뷰를 추가했습니다.'

    @validate_form
    @_validate_permission
    @validate_auth
    def put(self):
        """운동 리뷰 수정"""
        self.form.save()
        return '운동 리뷰를 수정했습니다.'

    @_validate_permission
    @validate_auth
    def delete(self):
        """운동 리뷰 삭제"""
        self.instance.delete()
        return '운동 리뷰를 삭제했습니다.'

class ReactedExerciseReviewService:
    def __init__(self, request:HttpRequest):
        self.request = request

    @validate_auth
    def post(self, exercise_review_id:int):
        """운동 리뷰 반응 추가/삭제"""
        exercise_review = get_object_or_404(ExerciseReview, pk=exercise_review_id)
        
        # 이전에 다른 반응을 추가했었다면 삭제
        prev_reaction = ReactedExerciseReview.objects.filter(
            user=self.request.user,
            exercise_review=exercise_review,
        ).exclude(
            emoji=self.request.POST['emoji'],
        ).first()
        prev_reaction and prev_reaction.delete()
        
        obj, created = ReactedExerciseReview.objects.get_or_create(
            user=self.request.user,
            exercise_review=exercise_review,
            emoji=self.request.POST['emoji'],
        )
        if created:
            return '운동 리뷰 반응을 추가했습니다.'
        else:
            obj.delete()
            return '운동 리뷰 반응을 삭제했습니다.'