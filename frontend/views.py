from django.shortcuts import render

def example(request):
    data_list = [
        {
            "id": 1,
            "content": "내용1",
            "tag": "태그1",
        },
        {
            "id": 2,
            "content": "내용2",
            "tag": "태그2",
        },
    ]
    return render(request, 'example/home.html', {'data_list': data_list})


def componentpage(request):
    return render(request,"pages/component_page.html")

def cyclepage(request):
    return render(request,"pages/cycle_page.html")

def scrappage(request):
    return render(request,"pages/scrap_page.html")

def restpage(request):
    return render(request,"pages/rest_page.html")

def periodpage(request):
    return render(request,"pages/period_page.html")

def componentcalendar(request):
    return render(request,"pages/component_calendar.html")

def mypage(request):
    return render(request,"pages/mypage.html")

def friendpage(request):
    return render(request,"pages/friend_page.html")

def editpage(request):
    return render(request,"pages/edit_page.html")
    