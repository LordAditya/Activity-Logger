from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, MyPostListView
from . import views


urlpatterns = [
    path('home', PostListView.as_view(), name='blog-home'),
    path('',views.welcome,name='blog-welcome'),
    path('user/<str:user>/calendar', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'),
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),
    #path('pics/', PicsListView.as_view(), name='blog-pics'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:user>/me', MyPostListView.as_view(), name='my-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    #path('pics/new/', PicsCreateView.as_view(), name='pics-create'),
   
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #path('about/',views.about, name='blog-about'),
]
