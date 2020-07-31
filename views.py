from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import City
# Create your views here.


def home(request):
    return render(request, "home.html")


def bar_chart(request):
    labels = []
    data = []

    q = City.objects.order_by('-popn')
    for city in q:
        labels.append(city.name)
        data.append(city.popn)

    return render(request, 'bar_chart.html', {
        'labels': labels,
        'data': data})


def line_chart(request):
    labels = []
    data = []

    q = City.objects.order_by('-popn')
    for city in q:
        labels.append(city.name)
        data.append(city.popn)

    return render(request, 'line_chart.html', {
        'labels': labels,
        'data': data})


def radar_chart(request):
    labels = []
    data = []

    q = City.objects.order_by('-popn')
    for city in q:
        labels.append(city.name)
        data.append(city.popn)

    return render(request, 'radar_chart.html', {
        'labels': labels,
        'data': data})