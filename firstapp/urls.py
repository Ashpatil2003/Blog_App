from . import views
from django.urls import path

from .views import login

urlpatterns=[
    path('',views.blog),
    path('login/',views.login,name='login'),
    path('signup/',views.signUp,name='signup'),
    path('home/',views.home),
    path('newpost/',views.newPost),
    path('mypost/',views.myPost),
    path('signout/',views.signOut)
]