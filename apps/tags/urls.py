from django.urls import path

from apps.tags import views

urlpatterns = [
    path('tags/',views.TagListView.as_view(), name='tag_index'),
    path('tags/create/',views.TagCreateView.as_view(), name='tag_create'),
    path('tags/detail/<int:pk>',views.TagDetailView.as_view(), name='tag_detail'),
    path('tags/delete/<int:pk>',views.TagDeleteView.as_view(), name='tag_delete'),
    path('tags/update/<int:pk>',views.TagUpdateView.as_view(), name='tag_update'),

]