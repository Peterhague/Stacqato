from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'name': 'Dave',
        'age': 26,
        'team': 'Luton Town FC'
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')

    return render(request, 'register.html')