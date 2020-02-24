from django.shortcuts import render,redirect
from .models import userlogin,registerDetail

# Create your views here.


def userloginView(request):
    if request.method == "POST":
        username = request.POST['username']
        userpass = request.POST['password']

        username = username.split()
        userpass = userpass.split()

        registerUser = registerDetail.objects.get(id=1)

        if(userpass == registerUser.password):
            return redirect("home/")
        else:
            message = "incorrect password.Please try again."
            return redirect("home/")
    else:
        username =''
        userpassword = ''
        message='GET'
        if 'username' in request.GET:
            user = request.GET['username']
            password = request.GET['password']

        return render(request,'loggingbase.html')

def registerUserView(request):
    if request.method == "POST":
        regDetail = registerDetail()
        regDetail.username = request.POST['registerName']
        regDetail.password = request.POST['registerPassword']
        regDetail.email = request.POST['registerEmailId']
        regDetail.save()
        message="You have been registered successfully."
        return redirect('/',{'msg':message})
    else:
        username =''
        userpassword = ''
        if 'username' in request.GET:
            user = request.GET['username']
            password = request.GET['password']

        return render(request,'loggingbase.html')
