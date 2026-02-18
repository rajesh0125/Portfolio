from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

   # return HttpResponse("My name is rajesh")

def about(request):
    return render(request, 'about.html')
   # return HttpResponse("My can know the details about me")

def project(request):
    return render(request, 'project.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html') 


