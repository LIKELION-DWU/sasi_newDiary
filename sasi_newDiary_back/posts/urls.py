from django.urls import path
from posts import views
from django.conf import settings
from django.conf.urls.static import static

app_name="posts"

urlpatterns = [
    path('', views.post_main, name='posts'),
    # post_create 로 수정함
    path('create',views.post_create, name='post_create'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
    # 댓글 
    path('create_comment/<int:post_id>', views.create_comment, name='create_comment'),

]





