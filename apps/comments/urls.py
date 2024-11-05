from django.urls import path
from apps.comments import views

urlpatterns = [
    path('comment_create/<int:pk>/', views.CommentCreateView.as_view(), name='com_create'),
    path('comment_update/<int:pk>/', views.CommentUpdateView.as_view(), name='com_update'),
    path('comment_delete/<int:pk>/', views.CommentDeleteView.as_view(), name='com_delete'),
]
