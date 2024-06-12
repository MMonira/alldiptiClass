from django.shortcuts import render
from backendapp.models import *
from backendapp.forms import *



def addtask(request):
    if request.method == 'POST':
        form = createtaskform(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            # f.category = 
    return render(request,'another/addtask.html')
