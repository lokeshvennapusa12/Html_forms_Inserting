from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
def Insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            sid=SFD.cleaned_data['sid']
            name=SFD.cleaned_data['name']
            age=SFD.cleaned_data['age']
            add=SFD.cleaned_data['address']
            resume=SFD.cleaned_data['resume']
            image=SFD.cleaned_data['image']
            
            SO=Student.objects.get_or_create(sid=sid,name=name,age=age,address=add,resume=resume,image=image)[0]
            SO.save()

            SQS=Student.objects.all()
            d1={'SQS':SQS}
            return render(request,'display_student.html',d1) 

    return render(request,'Insert_student.html',d)

def Insert_course(request):
    CFO=CourseForm()
    d={'CFO':CFO}

    return render(request,'Insert_course.html',d)

def display_student(request):
    SQS=Student.objects.all()
    d1={'SQS':SQS}
    return render(request,'display_student.html',d1) 



    
