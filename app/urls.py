from django.urls import path
from . import views 



app_name = 'app'

urlpatterns = [
    path('', views.RegistrationView, name='home'),
    path('register', views.register , name = 'register'),
    path('login', views.loginview, name='login' ),
    path('user-view', views.user_view, name="user_view"),
    path('vote/<int:id>',views.vote , name = "vote")
]