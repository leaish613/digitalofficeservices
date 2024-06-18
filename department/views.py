from django.shortcuts import render
from department.models import Department
# Create your views here.

def dep(request):
    if request.method=='POST':
        obj=Department()
        obj.name=request.POST.get('Deptname')
        obj.save()
    return render(request, 'department/department.html')




