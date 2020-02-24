from django.db import models

# Create your models here.

class usertaskList(models.Model):
    taskName = models.TextField(max_length=30,null=False)
    taskId = models.TextField(max_length=10)
    taskDesc = models.TextField(max_length=150)
    taskPriority = models.TextField(max_length=4)
    taskStatus = models.TextField(max_length=20)

    def __str__(self):
        return self.taskName
