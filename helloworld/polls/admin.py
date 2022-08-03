from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문', {'fields': ['question_text']}),
        ('작성 일자', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('질문', {'fields': ['question', 'choice_text']}),
        ('투표 수', {'fields': ['votes']}),
    ]
    list_display = ('choice_text', 'votes')
    list_filter = ['votes']
    search_fields = ['choice_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
