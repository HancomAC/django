from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Comment
from django.urls import reverse


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(title=query)
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostLV, self).get_context_data(**kwargs)
        if self.request.GET.get('q'):
            context['q'] = self.request.GET.get('q')
        return context


class PostSearch(ListView):
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(title__contains=query)
        return qs


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDV, self).get_context_data(**kwargs)
        if self.request.session.get('read-' + str(context['post'].id), True):
            context['post'].view += 1
            context['post'].save()
        self.request.session['read-' + str(context['post'].id)] = False
        context['writer'] = self.request.session.get('writer', '')
        return context


class CommentAdd(CreateView):
    model = Comment
    fields = ['writer', 'content', 'post']

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.object.post.slug})

    def post(self, request, *args, **kwargs):
        request.session['writer'] = request.POST.get('writer')
        return super(CommentAdd, self).post(request, *args, **kwargs)
