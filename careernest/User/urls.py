from django.urls import path
from .views import StudentsView,SignUpView,StudentDataView,CustomAuthToken
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',StudentsView.as_view()),
    path('signup',SignUpView.as_view()),
    path('login',CustomAuthToken.as_view(),name='login'),
    path('user-onboard/<int:pk>',StudentDataView.as_view()),
    
    
]