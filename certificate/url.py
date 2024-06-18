from django.conf.urls import url
from certificate import views

urlpatterns=[
    url('add/',views.cer),

    url('view/',views.view),
]