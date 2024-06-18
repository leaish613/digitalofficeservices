from django.db import models

# Create your models here.
class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    contact_no = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    d_id = models.IntegerField()
    batch = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    f_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'students'

