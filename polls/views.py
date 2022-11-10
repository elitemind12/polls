from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'latest_list'

    def get_queryset(self):
        '''return latest five question to be published'''
        return Question.objects.order_by('-p_date')[:5]

class DetailView(generic.DetailView):

    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):

    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': 'you dont select a choice'
        }
        return render(request, 'polls/detail.html',context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # ... Always return an HttpResponseRedirect after successfully dealing
        # ... with POST data. This prevents data from being posted twice if a
        # ... user hits the Back button
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



'''
# Render home page ....
def index(request):
    latest_list = Question.objects.order_by('-p_date')[:10]
    context = {'latest_list' : latest_list}
    return render(request,'polls/index.html',context)

# Render details page ....

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# Render vote page ....
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': 'you dont select a choice'
        }
        return render(request, 'polls/detail.html',context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # ... Always return an HttpResponseRedirect after successfully dealing
        # ... with POST data. This prevents data from being posted twice if a
        # ... user hits the Back button
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# Render results page ....   
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)
'''