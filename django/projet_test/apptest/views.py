from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from apptest.form import QuestionForms

from apptest.models import Questions

def index(request):
    questions = Questions.objects.all()
    context = {'questions': questions,}
    return render(request,'apptest/index.html',context)

def create(request):
    context ={}
 
    form = QuestionForms(request.POST or None)
    if form.is_valid():
        form.save()
        
         
    context['form']= form
    return render(request,'apptest/create.html',context)

def update(request, id):
    context ={}
 
    
    obj = get_object_or_404(Questions, id = id)
 
    form = QuestionForms(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/apptest")
 
    context["form"] = form
    return render(request,'apptest/update.html',context)


def delete(request, id):
    context ={}
 
    
    obj = get_object_or_404(Questions, id = id)
 
    form = QuestionForms(request.POST or None, instance = obj)
    obj.delete()
    return HttpResponseRedirect("/apptest")