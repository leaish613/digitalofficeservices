from django.shortcuts import render
from faculty.models import Faculty
# Create your views here.

def faculty(request):
    if request.method=='POST':
        obj=Faculty()
        obj.name=request.POST.get('name')
        obj.d_id=request.POST.get('department')
        obj.contact_no=request.POST.get('phone')
        obj.email_id=request.POST.get('email')
        obj.save()
    return render(request,'faculty/faculty.html')

