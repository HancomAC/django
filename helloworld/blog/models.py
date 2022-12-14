from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField('제목', max_length=50)
    slug = models.SlugField('슬러그', allow_unicode=True, unique=True)
    description = models.CharField('설명', max_length=100, blank=True)
    content = models.TextField('내용')
    create_dt = models.DateTimeField('작성일', auto_now_add=True)
    modify_dt = models.DateTimeField('수정일', auto_now=True)
    view = models.IntegerField('조회수', default=0)

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
        db_table = 'blog_post'
        ordering = ['-modify_dt']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)


class Comment(models.Model):
    content = models.TextField('내용')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_dt = models.DateTimeField('작성일', auto_now_add=True)
    writer = models.CharField('작성자', max_length=20)
