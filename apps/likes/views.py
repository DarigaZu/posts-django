from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from apps.likes.models import Like
from apps.likes.forms import LikeForm
from apps.posts.models import Post


class LikeListView(generic.ListView):
    model = Like
    template_name = 'like/index.html'
    context_object_name = 'likes'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()  
        return context

class LikeCreateView(generic.CreateView):
    model = Like
    template_name = 'like/create.html'
    form_class = LikeForm
    success_url = reverse_lazy('like_index')  

class LikeDetailView(generic.DetailView):
    model = Like
    template_name = 'like/detail.html'
    context_object_name = 'like'

class LikeUpdateView(generic.UpdateView):
    model = Like
    template_name = 'like/update.html'
    form_class = LikeForm
    success_url = reverse_lazy('like_index')   
    
    def get_success_url(self):
        return reverse_lazy('like_detail', kwargs = {'pk' : self.object.pk})
    
class LikeDeleteView(generic.DeleteView):
    model = Like
    template_name = 'like/delete.html'
    success_url = reverse_lazy('like_index')       