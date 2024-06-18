from django.shortcuts import render
from student.models import Students
# Create your views here.

def stud(request):
    if request.method=='POST':
        obj=Students()
        obj.name=request.POST.get('name')
        obj.d_id='1'
        obj.address=request.POST.get('address')
        obj.batch=request.POST.get('batch')
        obj.contact_no=request.POST.get('phone')
        obj.email_id=request.POST.get('email')
        obj.year=request.POST.get('year')
        obj.f_id='1'
        obj.save()
    return render(request,'student/student.html')
