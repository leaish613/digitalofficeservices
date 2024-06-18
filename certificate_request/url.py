from django.conf.urls import url
from certificate_request import views
urlpatterns = [
    url('req/(?P<idd>\w+)',views.req),
    url('reject/(?P<idd>\w+)',views.reject),
    url('rejectadmin/(?P<idd>\w+)',views.rejectadmin),
    url('send/(?P<idd>\w+)',views.send),

    url('view/',views.view),
    url('viewfaculty/',views.viewfaculty),
    url('viewstatus/',views.viewstatus)
]