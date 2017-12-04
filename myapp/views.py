from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import QuestionTian as Question,Choice
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

def index(request):

    latest_question_list = Question.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list} # 指定返回的结果字段名称
    print context
    return render(request, 'myapp/index.html', context)

# def detail(request,question_id):
#
#
#     question=get_object_or_404(Question,pk=question_id)
#
#     return render(request,'myapp/detail.html',{'question':question})

class DetailView(generic.DetailView):

    model = Question
    template_name = 'myapp/detail.html'
    #context_object_name = 'question1'

# def results(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'myapp/results.html', {'question': question})


class ResultView(generic.DetailView):

    model = Question
    template_name = 'myapp/results.html'
    context_object_name ='question'

def vote(request, question_id):

    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'myapp/detail.html',{
            'question':p,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myapp:results',args=[p.id])) # reverse反转URL，根据指定的name得到url地址