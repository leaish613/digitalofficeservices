from django.db import models

# Create your models here.

class Faculty(models.Model):
    f_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    d_id = models.IntegerField()
    contact_no = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'faculty'

