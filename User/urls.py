from django.conf.urls import url
from . import views

app_name = 'User'   # 这里是为了url反向解析用

urlpatterns = [
    # 这里放映射的view
    url(r'^$', views.index, name="index"),  # 首页
    url(r'^search/$', views.index, name="index"),  # 接收问题


    url(r'^theinput/$', views.theinput, name="theinput"),
    url(r'^question/$', views.question, name="question"),

    #视频课
    url(r'^$',views.search_answer,name="search_answer"),

    #自己测试
    url(r'^test(\d+)$', views.test, name="test"),
]
