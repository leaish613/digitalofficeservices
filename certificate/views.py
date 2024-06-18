from django.shortcuts import render
from certificate.models import Certificate

# Create your views here.
def cer(request):
    if request.method=='POST':
        obj=Certificate()
        obj.name=request.POST.get('name')
        obj.save()
    return render(request,'certificate/certificate.html')


def view(request):
    obj=Certificate.objects.all()
    context={
        'a':obj
    }
    return render(request,'certificate/viewcertificate.html',context)