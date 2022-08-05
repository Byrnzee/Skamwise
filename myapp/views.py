from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import PostForm, WarningBlock, SafeBlock
from .checks import urlCompare


def new(request):
    form = PostForm(request.Post)
    return render(request, "blog/base.html", {"form": form})                # Create Webpage

def urlchecker(request):

    if request.method == 'POST':                                            # If we get in a URL
        form = WarningBlock(request.POST)                                   # Create it
        if form.is_valid():                                                 # And if it's Valid
            if urlCompare(request.POST["search_box"]):                      # And if its in our List
                return render(request,"blog/Warning.html",{"form": form})   # Render warning
            else:
                return render(request,"blog/Safe.html",{"form": form})      # or else render its safe
    else:
        form = PostForm()
    return render(request, 'blog/base.html', {'form': form})







#def search_bar(request):
#    if request.method == 'GET':
#        search_query = request.GET.get('search_box', None)


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#     return render(request, 'home.html', {'form': form})


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
