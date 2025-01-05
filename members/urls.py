from django.urls import path
from .views import RegisterView, UserDashboardView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('dashboard/', UserDashboardView.as_view(), name='user_dashboard'),

]