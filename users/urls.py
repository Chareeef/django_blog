from django.urls import path
from django.contrib.auth.views import LoginView
import users.views as user_views

urlpatterns = [
    path('register/', user_views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('profile/', user_views.profile_view, name='profile'),
]
