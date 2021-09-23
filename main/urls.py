from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('check_user', views.check_user, name="Check_user"),
    path('sign_up/',views.sign_up, name="Sign_up"),
    path('new_user', views.new_user, name="New_user"),
    path('<str:user>/<str:password>/', views.dashboard, name="Dashboard"),
    path('delete/<str:user>/<str:password>/<int:id>/', views.delete, name="Delete")
]