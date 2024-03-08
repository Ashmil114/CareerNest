from django.urls import path
from .views import JobsView,JobView


urlpatterns = [
    path('',JobsView.as_view()),
    path('more/<int:pk>',JobView.as_view()),
    
    
]