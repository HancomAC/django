import datetime

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from polls.models import Question, Choice


# Create your views here.
def index(request):
    page = int(request.GET.get('page', 1))
    lastest_question_list = Question.objects.all().order_by('-pub_date')[page * 5 - 5:][:5]
    return render(request, 'polls/index.html', {'lastest_question_list': lastest_question_list, 'page': page,
                                                'maxpage': len(Question.objects.all()) // 5 + 1})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error': '항목을 선택하세요.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return HttpResponseRedirect(reverse('polls:index'))


def add_question(request):
    question = Question(question_text=request.POST['question_text'], pub_date=datetime.datetime.now())
    question.save()
    return HttpResponseRedirect(reverse('polls:index'))


def add_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = Choice(question=question, choice_text=request.POST['choice_text'], votes=0)
    choice.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
