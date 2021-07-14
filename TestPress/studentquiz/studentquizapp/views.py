from django.shortcuts import render
from studentquizapp.forms import QuestionForm
from studentquizapp.models import Question
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.

lst=[]
anslist=[]
obj = Question.objects.all()
for i in obj:
    anslist.append(i.crtanswer)
def login_view(request):
    return render(request,'testapp/login.html')

def ins_view(request):
    return render(request,'testapp/ins.html')

def subject_view(request):
    return render(request,'testapp/subject.html')

def engqus1_view(request):
    obj = Question.objects.all()
    paginator = Paginator(obj,1)
    try:
        page= int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        questions=paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)
    return render(request,'testapp/english.html',{'obj':obj,'questions':questions})

def result_view(request):
    form=QuestionForm()
    if request.method=='GET':
        form=QuestionForm(request.GET)
        if form.is_valid():
            form.save()
    score=0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score+=1
    return render(request,'testapp/result.html',{'score':score})

def saveans_view(request):
    ans = request.GET['ans']
    print(ans)
