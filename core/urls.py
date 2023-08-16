from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.login_auth,name="login"),
    path('singup/',views.singup,name="singup"),
    path('home/',views.home,name="home"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
]
