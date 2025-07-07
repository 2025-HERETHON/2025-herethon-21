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
    def read_reviewrating(user, date):
        return ConditionReview.objects.filter(user=user, date=date).values_list('rating', flat=True).first()
    '''
    flat=True ex) [3, 4, 5]를 [(3,), (4,), (5,)]로 반환한다.
    튜플 바로 뒤에 붙는 콤마는 파이썬 문법!
    '''
    
    @staticmethod
    def delete_review(user, date):
        review = ConditionReview.objects.filter(user=user, date=date).first()
        if not review:
            raise ValidationError("삭제할 리뷰가 존재하지 않습니다.")
        review.delete()
        
    @staticmethod
    def update_review(review: ConditionReview, data):
        rating = data.get("rating")
        if rating is not None:
            review.rating = int(rating)
        review.comment = data.get("comment", review.comment)
        review.save()
        return review

