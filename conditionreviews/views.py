from django.shortcuts import render
from .services import ConditionReviewService
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
def create_ConditionReview(request):
    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        date_str = request.POST.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()

        try:
            ConditionReviewService.create_review(
                request.user, 
                date,
                rating,
                comment
                )


            context = {
                "rating":rating,
                "comment":comment
            }
            return render(request, 'main.html', context)
        except ValidationError as e:
            return render(request, "create.html", {"error": str(e)})
        except IntegrityError as e:
            return render(request, "create.html", {"error": "같은 날짜에 이미 리뷰를 작성했습니다."})
        except Exception as e:
            return render(request, "create.html", {"error": "알 수 없는 오류가 발생했습니다."})
    return render(request, "create.html")

@login_required
def read_ConditionReview(request, date_str):
    try:
        # 문자열 → date 객체로 변환
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return render(request, "read.html", {"error": "날짜 형식이 올바르지 않습니다."})

    review = ConditionReviewService.get_review_by_date(request.user, date)

    return render(request, "read.html", {
        "review": review,
        "selected_date": date_str
    })