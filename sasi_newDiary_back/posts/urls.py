from django.urls import path
from posts import views


app_name="posts"

urlpatterns = [
    path('', views.post_main, name='main'),
    # 게시글
    path('post_create',views.post_create, name='post_create'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:id>', views.post_detail, name='post_detail'),
    path('post_update/<int:id>/', views.post_update, name="post_update"),
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),
    # 댓글 
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),

]





