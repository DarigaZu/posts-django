from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from apps.users.forms import UserUpdateForm, UserCreateForm

User = get_user_model()


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('/')

class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('/')

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'        