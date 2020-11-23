from django.urls import path
# from calc import views
from travello import views

urlpatterns = [
    path('', views.home, name= 'home')
]
