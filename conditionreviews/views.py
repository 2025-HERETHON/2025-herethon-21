from django.shortcuts import render
from .services import ConditionReviewService
from django.utils import timezone
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from datetime import datetime



# Create your views here.
def create_ConditionReview(request):
    print("요청 들어옴:" , request.method)
    if request.method == "POST":
        print("POST 요청 감지됨")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        date_str = request.POST.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        print(rating)
        print(comment)
        print(date)
        try:
            ConditionReviewService.create_review(
                request.user, 
                date,
                rating,
                comment
                )
            print("DB 저장 시도")


            context = {
                "rating":rating,
                "comment":comment
            }
            return render(request, 'main.html', context)
        except ValidationError as e:
            print("ValidationError 발생:", e)
            return render(request, "create.html", {"error": str(e)})
        except IntegrityError as e:
            print("IntegrityError 발생:", e)
            return render(request, "create.html", {"error": "같은 날짜에 이미 리뷰를 작성했습니다."})
        except Exception as e:
            print("기타 Exception 발생:", e)
            return render(request, "create.html", {"error": "알 수 없는 오류가 발생했습니다."})
    return render(request, "create.html")