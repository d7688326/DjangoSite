from django.contrib import admin
from article.models import Article, Comment,Procedure,Bookmark

# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Procedure)
admin.site.register(Bookmark)