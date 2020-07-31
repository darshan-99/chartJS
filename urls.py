from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home', views.home, name="home"),
    url(r'^bar_chart', views.bar_chart, name="bar_chart"),
    url(r'^line_chart', views.line_chart, name="line_chart"),
    url(r'^radar_chart', views.radar_chart, name="radar_chart"),
]