from django.shortcuts import render, redirect
from .forms import MyForm
from .models import Client

#My Views

def FormView(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('success_url')
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})