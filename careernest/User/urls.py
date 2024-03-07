from django.urls import path
from .views import StudentsView,SignUpView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',StudentsView.as_view()),
    path('signup',SignUpView.as_view()),
    path('login',obtain_auth_token,name='login')
]