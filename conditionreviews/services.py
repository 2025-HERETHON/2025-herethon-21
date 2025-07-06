from .models import ConditionReview
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class ConditionReviewService:
    @staticmethod
    def create_review(user, date, rating, comment):
        try:
            if not rating:
                raise ValidationError("표정을 선택해주세요.")
            
            ConditionReview.objects.create(
                user=user,
                date=date,
                rating=int(rating),
                comment=comment
            )
            print("DB 저장 성공")
        except IntegrityError as e:
            print("IntegrityError:", e)
            raise ValidationError("같은 날짜에는 한 번만 작성할 수 있습니다.")
        except Exception as e:
            print("Exception 발생:", e)
            raise ValidationError(f"알 수 없는 오류: {str(e)}")

                