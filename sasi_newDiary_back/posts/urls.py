from django.urls import path
from posts import views

app_name="posts"

urlpatterns = [
    path('',views.post_main,name='main'),
    path('post_list/', views.post_list, name='post_list'),
    path('create/', views.create, name='post_create'),
    path('detail/<int:id>/', views.post_detail, name='post_detail'),
    path('update/<int:id>/', views.post_update, name="post_update"),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
]




