from django.shortcuts import render
def index(request):
  return  render(request,'index.html')
def About(request):
  return render(request, 'about.html')
def Contact(request):
  return render(request, 'contact.html')
def login(request):
  return render(request, 'login.html')
def register(request):
  return render(request, 'register.html')
def services(request):
  return render(request, 'services.html')
def tables(request):
  return render(request, 'tables.html')
def utilitiesanimation(request):
  return render(register, 'utilities-animation.html')
