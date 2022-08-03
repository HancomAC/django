from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Comment
from django.urls import reverse_lazy


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class CommentAdd(CreateView):
    model = Comment
    fields = ['name', 'email', 'body']
    template_name = 'blog/comment_form.html'
    success_url = reverse_lazy('blog:post_detail')
