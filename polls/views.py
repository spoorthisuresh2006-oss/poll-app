from django.shortcuts import render, redirect
from .models import Question

def index(request):
    latest_question = Question.objects.first()
    return render(request, 'polls/index.html', {'question': latest_question})

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)

    if 'choice' not in request.POST:
        return render(request, 'polls/index.html', {
            'question': question,
            'error_message': "Please select a choice first.",
        })

    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()

    return redirect('polls:index')