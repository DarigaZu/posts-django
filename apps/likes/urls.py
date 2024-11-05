from django.urls import path
from apps.likes import views

urlpatterns = [
    path('likes/', views.LikeListView.as_view(), name='like_index'),
    path('likes/create/<int:pk>/', views.LikeCreateView.as_view(), name='like_create'),
    path('likes/detail/<int:pk>/', views.LikeDetailView.as_view(), name='like_detail'),
    path('likes/delete/<int:pk>/', views.LikeDeleteView.as_view(), name='like_delete'),
    path('likes/update/<int:pk>/', views.LikeUpdateView.as_view(), name='like_update'),
]
