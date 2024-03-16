from django.urls import path,include
from .views import Home

urlpatterns = [
    path('',Home),
    path('user/',include('User.urls')),
    path('staff/',include('Staff.urls'))
    
]