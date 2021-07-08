from django.urls import path
from . import views 



app_name = 'app'

urlpatterns = [
    path('', views.RegistrationView, name='home'),
    path('register', views.register , name = 'register')
]