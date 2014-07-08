from django.db import models
from django.contrib.auth.models import User
from article.models import get_upload_file_name

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    intro= models.CharField(max_length=100,default="introduce yourself here !")
    photo = models.ImageField(upload_to=get_upload_file_name,default='media/default_photo.jpg',blank=True)

# if object exist get it, if not create one
User.profile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])

