from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import ProfileForm
# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registration.html',{'form':form})

def dashboard(request):
    return render(request,'dashboard.html')

def addprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm()
    return render(request, 'addprofile.html', {'form': form})

def home(request):
    return render(request,'home.html')