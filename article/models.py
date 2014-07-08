from django.db import models
from time import time
from django.utils import timezone
from django.conf import settings
from mytravel import settings
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Avg

def get_upload_file_name(instance,filename):
    return 'media/%s_%s' %(str(time()).replace('.','_'),filename)

def get_avg(article_id):
    avg_rating = Article.objects.filter(id=article_id).aggregate(average= Avg('comment__rating'))
    return avg_rating['average']

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    materials=models.CharField(max_length=200)
    body = models.TextField()
    pub_date= models.DateTimeField('date published',default=timezone.now())
    likes = models.IntegerField(default=0)
    thumbnail=models.FileField(upload_to=get_upload_file_name,default='media/default_photo2.jpg')
    cooktime=models.IntegerField(default=0)
    difficulty=models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)])
    steps = models.IntegerField(default=0,validators=[MaxValueValidator(20)])
    author = models.CharField(default='Admin',max_length=50)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/articles/get/%i/" %self.id

    def get_thumbnail(self):
        thumb = str(self.thumbnail)
        return thumb




class Comment(models.Model):
    CHOICES=(
        ('1','so bad'),
        ('2','not bad'),
        ('3','OK'),
        ('4','good'),
        ('5','excellent')
    )
    name= models.CharField(max_length=100)
    body= models.TextField()
    pubdate= models.DateTimeField('date published')
    rating = models.CharField(choices=CHOICES,default='excellent',max_length=2)
    #article field is linked to class Article
    article=models.ForeignKey(Article)

    def __unicode__(self):
        return self.name



class Procedure(models.Model):

    url_height =models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")
    url_width =models.PositiveIntegerField(null=True, blank=True, editable=False, default="200")

    description = models.TextField(max_length=500)
    picture = models.ImageField(upload_to=get_upload_file_name,height_field='url_height', width_field='url_width',blank=True)
    article = models.ForeignKey(Article)

    def get_picture(self):
        pic= str(self.picture)
        return pic

class Bookmark(models.Model):
    user_id = models.IntegerField(default=1)
    article_id= models.IntegerField(default=1)

    class Meta:
        unique_together=('user_id','article_id')

