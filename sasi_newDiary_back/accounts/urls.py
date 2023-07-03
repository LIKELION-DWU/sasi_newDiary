from django.urls import path
from accounts import views
urlpatterns = [
    path('', views.home, name='login'),
    path('signup', views.signup, name='signup'),
]
