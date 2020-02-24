from django.shortcuts import render,redirect
from .models import userlogin,registerDetail

# Create your views here.


def userloginView(request):
    if request.method == "POST":
        username = request.POST['username']
        userpass = request.POST['password']

        registerUser = registerDetail.objects.get(username="pavan kranthi")
        print(registerUser.password)
        print(userpass)

        if(userpass == registerUser.password):
            print("hello" + username)
            return redirect("home/",{'uname':username})
        else:
            message = "incorrect password.Please try again."
            return render(request,'loggingbase.html',{'errorMsg':message})
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
