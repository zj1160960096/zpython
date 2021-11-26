from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.hello),
]


urlpatterns = [
    path('runoob/', views.runoob),
]