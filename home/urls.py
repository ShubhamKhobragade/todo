from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logout_view,name='index'),
    path('register',views.register,name='register'),
]
