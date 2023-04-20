from django import forms

g=[('male','male'),('female','female')]

c=[('python','Python'),('java','Java'),('sql','Sql'),('django','Django')]
#s=Student.objects.all()

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    resume=forms.FileField()
    image=forms.ImageField()

class CourseForm(forms.Form):
    cid=forms.IntegerField()
    sid=forms.ChoiceField()
    cname=forms.CharField(max_length=50)
    ctrainer=forms.CharField(max_length=100)

    