from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home),
    path(r'signup/', views.signup),
    path(r'forgotPassword/', views.forgotPassword),
    path(r'change_password/', views.changePassword),

]
