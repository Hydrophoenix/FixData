from django.shortcuts import render

# Create your views here.
def dashboard(request):
    '''a function for index page display'''
    return render(request, "dashboard2.html")
