from django.urls import path, include
from account.views import registration_view, success_view, change_view

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('change', change_view, name='change'),
    path('', include('django.contrib.auth.urls')),
    path('success/', success_view, name='success'),
]
