
from django.urls import path
from . import views




urlpatterns = [
    path('hello', views.say_hello, name='say_hello'),
    path('', views.home, name='home'),
    path('menu/', views.MenuItemGenericView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemGenericView.as_view()),
    
]