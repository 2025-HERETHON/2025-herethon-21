from django.shortcuts import render, redirect,  get_object_or_404
from .services import ConditionReviewService
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import ConditionReview
from django.http import HttpResponseForbidden



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
            return redirect('accounts:main')
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

    review = ConditionReviewService.read_review(request.user, date)

    return render(request, "read.html", {
        "review": review,
        "selected_date": date_str
    })

@login_required
def read_ConditionReviewRating(request, date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return render(request, "read.html", {"error":"날짜 형식이 올바르지 않습니다."})
    
    review_rating = ConditionReviewService.read_review_rating(request.user, date)
    
    return render(request, "read.html", {"review_rating":review_rating})
    
@login_required
def delete_ConditionReview(request, date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return render(request, "read.html", {"error": "날짜 형식이 올바르지 않습니다."})

    try:
        ConditionReviewService.delete_review(request.user, date)
        return redirect("accounts:main")  # 삭제 후 메인화면으로
    except ValidationError as e:
        return render(request, "read.html", {"error": str(e), "selected_date": date_str})
    except Exception as e:
        return render(request, "read.html", {"error": "알 수 없는 오류가 발생했습니다.", "selected_date": date_str})
    
@login_required
def update_ConditionReview(request, date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return HttpResponseForbidden("잘못된 날짜 형식입니다.")

    review = get_object_or_404(ConditionReview, user=request.user, date=date)

    choices = review._meta.get_field("rating").choices

    if request.method == "POST":
        ConditionReviewService.update_review(review, request.POST)
        return redirect("conditionreviews:read_ConditionReview", date_str=date_str)

    context = {
        "review": review,
        "selected_date": date_str,
        "rating_choices": choices,   # 추가
    }
    return render(request, "review_update.html", context)
