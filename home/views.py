from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# khobragades244@gmail.com  Sonu!@#123
# shubham866  Shubham@121
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'index.html')

def loginUser(request):
    if request.method == 'POST':
        # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/register')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username, 'lennon@thebeatles.com', password)
        user.last_name = username
        user.save()
        if user is not None:
            login(request,user)
            return redirect('/login')
        else:
            return redirect('/register')
    return render(request,'regis.html')

def logout_view(request):
    logout(request)
    return redirect('/login')
# Create your views here.
