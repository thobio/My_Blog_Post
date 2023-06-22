from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name='login'),
    path('forgotpassword/', views.user_forgot_password, name='forgot_password'),
    path('logout/', views.user_logout, name='logout'),
    path('activate/<email_token>', views.activate_email, name='activate'),
]
