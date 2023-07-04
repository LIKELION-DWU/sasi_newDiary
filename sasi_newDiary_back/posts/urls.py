from django.urls import path
from posts import views
from django.conf import settings
from django.conf.urls.static import static

app_name="posts"

urlpatterns = [
    path('', views.post_main, name='posts'),
    path('post_list/', views.post_list, name='post_list'),
    path('create',views.create,name='post_create'),
]




