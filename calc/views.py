from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.checks import messages
from django.shortcuts import render, redirect


# Create your views here.
from calc.decorator import unauthenticated_user
from calc.forms import CreateUserForm
from calc.models import Customer

@login_required(login_url='signin')
def home(request):

    context={'name':'dear user'}
    return render(request,'accounts/home.html',context)


@login_required(login_url='signin')
def add(request):
    number1=int(request.GET["num1"])
    number2=int(request.GET["num2"])

    add=number2+number1
    return render(request,'accounts/add.html',{'add':add})

@unauthenticated_user
def singup(request):
    formSet=CreateUserForm()
    if request.method=="POST":
        formSet=CreateUserForm(request.POST)
        if formSet.is_valid():
            user=formSet.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email
            )
            return redirect('signup')
    context={'formSet':formSet}
    return render(request,'accounts/signup.html',context)


@unauthenticated_user
def signin(request):

    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            context = {'message':'wrong pass or username'}
            return render(request, 'accounts/signin.html', context)

    context={}
    return render(request,'accounts/signin.html',context)



def signout(request):
    logout(request)
    return redirect('signup')



