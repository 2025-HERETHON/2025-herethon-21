from django.shortcuts import render, redirect,  get_object_or_404
from .services import ConditionReviewService
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import ConditionReview
from django.http import HttpResponseForbidden
from utils.choices import ReactionEmojiType 
from datetime import date


def create_ConditionReview(request, date_str):
    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        print(f">> POST 받은 rating: {rating}")
        print(f">> POST 받은 comment: {comment}")
        try:
            ConditionReviewService.create_review(
                request.user,
                date_str,
                rating,
                comment
            )
            return redirect(request.META.get('HTTP_REFERER', '/')) 
        except ValidationError as e:
            return render(request, 'pages/mypage_main.html', {
                "error": str(e),
                "rating_choices": ReactionEmojiType.choices  # 에러 시에도 넘겨줌
            })
        except IntegrityError:
            return render(request,  "pages/mypage_main.html", {
                "error": "같은 날짜에 이미 리뷰를 작성했습니다.",
                "rating_choices": ReactionEmojiType.choices
            })
        except Exception:
            return render(request,  "pages/mypage_main.html", {
                "error": "알 수 없는 오류가 발생했습니다.",
                "rating_choices": ReactionEmojiType.choices
            })

    # GET 요청일 때 choices 넘기기
    return render(request, 'pages/mypage_main.html', {
        "rating_choices": ReactionEmojiType.choices
    })

@login_required
def read_ConditionReview(request, date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return render(request, "pages/mypage_main.html", {"error": "날짜 형식이 올바르지 않습니다."})

    review = ConditionReviewService.read_review(request.user, date)

    return render(request, "pages/mypage_main.html", {
        "review": review,
        "selected_date": date_str,
        "rating_choices": ReactionEmojiType.choices
    })

@login_required
def read_ConditionReviewRating(request, date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return render(request, "pages/mypage_main.html", {"error":"날짜 형식이 올바르지 않습니다."})
    
    review_rating = ConditionReviewService.read_review_rating(request.user, date)
    
    return render(request, "pages/mypage_main.html", {"review_rating":review_rating})
    
@login_required
def delete_ConditionReview(request, date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return render(request, "pages/mypage_main.html", {"error": "날짜 형식이 올바르지 않습니다."})

    try:
        ConditionReviewService.delete_review(request.user, date)
        return redirect(request.META.get('HTTP_REFERER', '/')) 
    except ValidationError as e:
        return render(request, "pages/mypage_main.html", {"error": str(e), "selected_date": date_str})
    except Exception as e:
        return render(request, "pages/mypage_main.html", {"error": "알 수 없는 오류가 발생했습니다.", "selected_date": date_str})
    
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
    return render(request, "pages/mypage_main.html", context)