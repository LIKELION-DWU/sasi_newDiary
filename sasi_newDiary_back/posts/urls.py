from django.urls import path
from posts import views

app_name="posts"

urlpatterns = [
    path('', views.post_main, name='posts'),
    path('post_list/', views.post_list, name='post_list'),
]
