from django.urls import path
from .views import home, register, login_view, profile, course_registration, confirm_fees, change_password, logout_view
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('course_registration/', course_registration, name='course_registration'),
    path('confirm_fees/', confirm_fees, name='confirm_fees'),
    path('change_password/', change_password, name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('course_registration_preview/<int:pk>/', views.course_registration_preview, name='course_registration_preview'),
]
