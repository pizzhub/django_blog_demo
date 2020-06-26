from django.shortcuts import render
from apps.personal.models import Question
from apps.account.models import Account


def home(request):
    print(request.headers)
    context = {}

    questions = Question.objects.all()
    accounts = Account.objects.all()
    print(accounts)
    context['accounts'] = accounts
    context['questions'] = questions

    return render(request, 'personal/home.html', context)

