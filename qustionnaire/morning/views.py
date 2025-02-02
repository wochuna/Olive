from django.shortcuts import render, redirect
from .forms import MyForm

#My View

# Form View
def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():

            feedback = form.save(commit=False)
            feedback.month = ','.join(form.cleaned_data['month'])
            feedback.save()
            return redirect('success')
    else:
        form = MyForm()
    return render(request, 'morning/form.html', {'form': form})

# Success View
def success_view(request):
    return render(request, 'morning/success.html')
