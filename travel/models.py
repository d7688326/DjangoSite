from django.db import models

# Create your models here.
class email(models.Model):
    email_id= models.AutoField(primary_key=True)
    Sender = models.CharField(max_length=30)
    Receiver= models.CharField(max_length=30)
    Send_date=models.DateField(auto_now=True)
    subject=models.TextField
    mail=models.TextField



