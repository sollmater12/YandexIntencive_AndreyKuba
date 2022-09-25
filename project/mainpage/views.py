from django.shortcuts import render
from django.http import HttpResponse


def mainpage(request):
    return HttpResponse(render(request, 'mainpage/html/mainpage.html', {'title': 'Главная Страница'}))
