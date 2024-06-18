from django.db import models

# Create your models here.

class Request(models.Model):
    r_id = models.AutoField(primary_key=True)
    c_id = models.IntegerField()
    s_id = models.IntegerField()
    f_id = models.IntegerField()
    need = models.CharField(max_length=45)
    date = models.DateField()
    status = models.CharField(max_length=45)
    reject_reason = models.CharField(max_length=45)
    uploaded_documents = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'request'
