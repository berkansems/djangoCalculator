from django.urls import path

from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('result/',views.result, name='result'),
    path('signup/',views.singup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
]