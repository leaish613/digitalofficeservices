from django.conf.urls import url
from department import views

urlpatterns = [
    url('dep/', views.dep),

]