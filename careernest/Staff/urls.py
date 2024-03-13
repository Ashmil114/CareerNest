from django.urls import path
from .views import JobsView,JobView,ApplyJobView,CompanySignUpView, CompanyView,SaveJobView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('job',JobsView.as_view()),
    path("companies",  CompanyView.as_view(), name=""),
    path('sign-up',CompanySignUpView.as_view()),
    path('login',obtain_auth_token,name='login'),
    path('job/more/<int:pk>',JobView.as_view()),
    path('job/apply-job',ApplyJobView.as_view()),
    path('job/save',SaveJobView.as_view()),
    
    
    
]