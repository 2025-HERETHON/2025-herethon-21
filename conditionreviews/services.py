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
        except IntegrityError as e:
            raise ValidationError("같은 날짜에는 한 번만 작성할 수 있습니다.")
        except Exception as e:
            raise ValidationError(f"알 수 없는 오류: {str(e)}")

    
    @staticmethod
    def read_review(user, date):
        return ConditionReview.objects.filter(user=user, date=date).first()
    
    @staticmethod
    def delete_review(user, date):
        review = ConditionReview.objects.filter(user=user, date=date).first()
        if not review:
            raise ValidationError("삭제할 리뷰가 존재하지 않습니다.")
        review.delete()
