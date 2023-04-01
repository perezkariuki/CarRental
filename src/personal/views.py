from django.shortcuts import render
from personal.models import Question

# Create your views here.

def home_screen_view(request):

    context = {}
    # list_of_values =[]
    # list_of_values.append("First Entery")
    # list_of_values.append("Second Entery")
    # list_of_values.append("Third Entery")
    # list_of_values.append("Fourth Entery")
    # context['list_of_values'] = list_of_values

    questions = Question.objects.all()
    context['questions'] = questions

    return render(request, "personal/home.html", context)