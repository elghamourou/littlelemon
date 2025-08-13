
from django.urls import path
from . import views




urlpatterns = [
    path('hello', views.say_hello, name='say_hello'),
    path('', views.home, name='home'),
    path('bookings/', views.BookingView.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'})),
]