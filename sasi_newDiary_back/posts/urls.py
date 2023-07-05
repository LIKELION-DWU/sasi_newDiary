from django.urls import path
from posts import views

app_name="posts"

urlpatterns = [
    path('', views.post_main, name='posts'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/', views.post_detail, name='post_detail'),
    # 댓글 
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),

]
