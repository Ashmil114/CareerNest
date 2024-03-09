from django.urls import path
from .views import JobsView,JobView,ApplyJobView


urlpatterns = [
    path('',JobsView.as_view()),
    path('more/<int:pk>',JobView.as_view()),
    path('apply-job',ApplyJobView.as_view()),
    
    
    
]