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
    return render(request,"example/component_page.html")

def componentcalendar(request):
    return render(request,"example/component_calendar.html")

def mypage(request):
    return render(request,"example/mypage.html")