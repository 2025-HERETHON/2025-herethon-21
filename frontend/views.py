from django.shortcuts import render
import json

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

def routineingpage(request):
    data_list = [
        {
            "id": 1,
            "content": "준비 스트레칭",
            "details1": "텍스트",
            "details2": "텍스트",
            "details3": "텍스트",
            "time": 1, #타이머 테스트용으로 짧게 1분으로 설정해뒀습니다
            "image": "assets/img/fitnessdog.png", 
        },
        {
            "id": 2,
            "content": "스쿼트",
            "details1": "텍스트",
            "details2": "텍스트",
            "details3": "텍스트",
            "time": 5,
            "image": "assets/img/fitnessdog.png", 
        },
        {
            "id": 3,
            "content": "플랭크",
            "details1": "텍스트",
            "details2": "텍스트",
            "details3": "텍스트",
            "time": 3,
            "image": "assets/img/fitnessdog.png", 
        },
        {
            "id": 4,
            "content": "암서클",
            "details1": "텍스트",
            "details2": "텍스트",
            "details3": "텍스트",
            "time": 5,
            "image": "assets/img/fitnessdog.png", 
        },
        {
            "id": 5,
            "content": "마무리 스트레칭",
            "details1": "텍스트",
            "details2": "텍스트",
            "details3": "텍스트",
            "time": 4,
            "image": "assets/img/fitnessdog.png", 
        },
    ]
    return render(request,
                    "result_pages/routine_ing_page.html",
                    {
                        'data_list': data_list,
                        'data_list_json':json.dumps(data_list),
                    }
                ) 
