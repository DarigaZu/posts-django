from django.views import generic
from django.urls import reverse_lazy

from apps.posts.models import Post
from apps.posts.forms import PostCreateForm, PostUpdateForm


class PostLIstView(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'posts'

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'update.html'
    success_url = reverse_lazy('detail')      

    def get_success_url(self):
        return reverse_lazy('detail', kwargs = {'pk' : self.object.pk})  

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')    