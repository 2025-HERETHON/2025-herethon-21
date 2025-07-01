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