from django.shortcuts import render
from . import forms
from django.views.generic.edit import FormView
from .forms import NameForm

def regform(request):
    form = NameForm()
    if request.method == 'POST':
        form = NameForm(request.POST)
        html = 'we have recieved this form again'
    else:
        html = 'welcome for first time'
    return render(request, 'blog/signup.html', {'html': html, 'form': form})

from django.http import HttpResponseRedirect
from django.shortcuts import render



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})




# def register(request):
#   if request.method == 'POST':
#      form = UserCreationForm(request.POST)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         messages.success(request, f'Account created for{username}!')
#         return redirect('home.html')
# else:
#      form = UserCreationForm()
#   return render(request, 'home.html',{'form': form})
