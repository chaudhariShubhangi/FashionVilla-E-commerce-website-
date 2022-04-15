from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

def testing(request):
    return render(request, "base.html")

from django.shortcuts import render , redirect , HttpResponseRedirect

from django.views import View



