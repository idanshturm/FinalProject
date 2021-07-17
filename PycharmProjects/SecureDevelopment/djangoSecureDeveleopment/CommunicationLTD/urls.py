from django.urls import path

from . import views

urlpatterns = {
    path('', views.home),
    path(r'signup/', views.sign),
    path(r'change_password/', views.changePassword),

}
