from django.urls import path
from .views import home, profile, progress, exercises, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('progress/', progress, name='users-progress'),
    path('exercises/', exercises, name='users-exercises'),
]
