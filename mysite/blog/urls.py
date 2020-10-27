from django.urls import  path
from . import views

app_name = "blog"


urlpatterns = [
    path('/',views.PostListView.as_view(), name ='post_list' ),
    path('/about',views.AboutView.as_view() , name='about'),
    path('/post/<int:pk>',views.DetailView.as_view() , name='post_detail'),
    path('/post/new_post',views.PostCreateView.as_view() , name='new_post'),
    path('/post/edit/<int:pk>',views.PostUpdateView.as_view() , name='post_edit'),
    path('/post/delete/<int:pk>',views.PostDeleteView.as_view() , name='post_delete'),
    path('/drafts/',views.DraftListView.as_view() , name='post_draft_list'),
    
    path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve', views.add_comment_to_post, name='add_comment_to_post'),

]
