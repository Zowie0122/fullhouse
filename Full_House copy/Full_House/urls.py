"""Full_House URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fullhouseapi.views import happy_view,addHappy_view,sad_view,addSad_view, deleteSad_view,expectation_view,addExpectation_view,base_view,deleteExpectation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('happy/', happy_view),
    path('happy/addHappyThings/',addHappy_view),
    path('sad/', sad_view),
    path('sad/addSadThings/',addSad_view),
    path('sad/deleteSadThings/<int:sadThing_id>/',deleteSad_view),
    path('expectation/', expectation_view),
    path('expectation/addExpectations/',addExpectation_view),
    path('expectation/deleteExpectation/<int:expectation_id>/',deleteExpectation_view),
    path('',base_view),
]
