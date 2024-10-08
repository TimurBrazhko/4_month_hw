from django.urls import path
from user.views import (
    register_view,
    login_view,
    logout_view,
    profile_view
)

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
