from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='Register'),
    path('login/',views.LoginView.as_view(),name = 'login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),


]