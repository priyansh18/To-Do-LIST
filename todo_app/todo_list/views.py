# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            messages.success(request,('Item Sucessfully Added'))
            return render(request,'home.html',{'item' : all_items })

    else:
        all_items = List.objects.all()
        return render(request,'home.html',{'item' : all_items })

def about(request):
    my_name = 'Priyansh Singhal'
    return render(request , 'about.html' ,{'name' : my_name})    

def remove(request, task_id):
    item = List.objects.get(id=task_id)
    item.delete()
    messages.success(request,('Item Sucessfully Deleted'))
    return redirect('homepage')

def cross_off(request, task_id):
    item = List.objects.get(id=task_id)
    item.completed = True
    item.save()
    return redirect('homepage')    

def uncross(request, task_id):
    item = List.objects.get(id=task_id)
    item.completed = False
    item.save()
    return redirect('homepage')       