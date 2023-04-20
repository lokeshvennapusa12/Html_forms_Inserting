from django.db import models

class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=300)
    resume=models.FileField()
    image=models.ImageField()

    def __str__(self) -> str:
        return self.name
    

class Course(models.Model):
    cid=models.IntegerField(unique=True)
    sid=models.ForeignKey(Student,on_delete=models.CASCADE)
    cname=models.CharField(max_length=50)
    ctrainer=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.cname


