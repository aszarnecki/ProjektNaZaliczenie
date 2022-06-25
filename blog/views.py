from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from blog.models import Post


class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]


class DetailsView(DetailView):
    model = Post
    template_name = 'blog/details.html'
    slug_field = 'id'


class MyLoginView(LoginView):
    model = Post
    template_name = 'blog/login.html'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:blog-index')
    form_class = UserRegisterForm
    success_message = "Profil został poprawnie utworzony"
    model = User


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", 'post_content',)



class NewPostView(CreateView):
    template_name = 'blog/new.html'
    model = Post
    form_class = NewPostForm
    success_url = reverse_lazy('blog:blog-index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:blog-index')



class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update.html'
    fields = [
        "title",
        "post_content"
    ]
    success_url = reverse_lazy('blog:blog-index')
