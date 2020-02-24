from django.shortcuts import render,HttpResponse
from .models import usertaskList
from django.db.models import Count
# Create your views here.

def userhomeView(request):
    return render(request,'userhome.html')


def dashboardView(request):
    if request.method =="GET":
        username = request.GET['username']
    else:
        username = request.POST['username']
    print(username)
    return render(request,'dashboard.html',{'uname':username})


def addtaskView(request):
    if request.method =="POST":
        usertaskListObj = usertaskList()
        usertaskListObj.taskName = request.POST['taskName']
        usertaskListObj.taskId = request.POST['taskName'] + "_1"
        usertaskListObj.taskDesc = request.POST['taskDetails']
        usertaskListObj.taskPriority = "1"
        usertaskListObj.taskStatus = "Added - Not Yet Started."
        usertaskListObj.save()

        details = usertaskList.objects.all().aggregate(taskCount=Count('taskName'))
        tasklist = usertaskList.objects.all()

    else:
        details = usertaskList.objects.all().aggregate(taskCount=Count('id'))
        tasklist = usertaskList.objects.all()

    return render(request,'addTask.html',{'taskCount': details['taskCount'],'taskList':tasklist})


def taskdetailsView(request):
    return HttpResponse("<p> Hello , you have successfully added the task</p>")
    #return render(request,'taskdetails.html')
