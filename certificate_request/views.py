from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from certificate_request.models import Request
import datetime
from certificate.models import Certificate
# Create your views here.
def reject(request,idd):
    if request.method=='POST':
        obj=Request.objects.get(r_id=idd)
        obj.reject_reason=request.POST.get('message')
        obj.save()
    return render(request, 'certificate_request/rejectmessage.html')

def rejectadmin(request,idd):
    if request.method=='POST':
        obj=Request.objects.get(r_id=idd)
        obj.reject_reason=request.POST.get('reply')
        obj.save()
    return render(request, 'certificate_request/rejectmessageadmin.html')


def req(request,idd):
    obb=Certificate.objects.get(c_id=idd)
    context={
        'kk':obb
    }
    if request.method=='POST':
        obj=Request()
        obj.need=request.POST.get('need')
        obj.c_id=idd
        obj.f_id='1'
        obj.s_id='1'
        obj.date=datetime.datetime.today()
        obj.status="Pending"
        obj.uploaded_documents="no documents"
        obj.save()
    return render(request, 'certificate_request/requestcertificate.html',context)

def send(request,idd):
    if request.method=='POST':
        obj=Request.objects.get(r_id=idd)
        myfile=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.uploaded_documents=myfile.name
        obj.status = "Issued"
        obj.save()
    return render(request, 'certificate_request/senddocument.html')


def view(request):
    obj=Request.objects.all()
    context={
        'kk':obj
    }
    return render(request,'certificate_request/viewradmin.html',context)

def viewfaculty(request):
    obj=Request.objects.all()
    context={
        'b':obj
    }
    return render(request,'certificate_request/viewrfaculty.html',context)

def viewstatus(request):
    obj=Request.objects.all()
    context={
        'c':obj
    }
    return render(request,'certificate_request/viewstatus.html',context)
