from django.conf.urls import patterns,url,include
from article import views
from article.views import HelloTemplate
from api import ArticleResource



article_resource = ArticleResource()

urlpatterns= patterns('',
                      url(r'^hello$',views.hello,name="index"),
                      url(r'^hellot$',views.hello_template),
                      url(r'hellos$',views.hello_simple),
                      url(r'^helloc$',HelloTemplate.as_view()),
                      url(r'^all/$','article.views.articles',name='all_articles'),
                      url(r'^get/(?P<article_id>\d+)/$','article.views.article'),
                      url(r'^language/(?P<language>[a-z\-]+)/$','article.views.language'),
                      url(r'^create$','article.views.create'),
                      url(r'^like/$','article.views.like_article'),
                      url(r'^bookmark/$','article.views.add_bookmark'),
                      url(r'^add_comment/(?P<article_id>\d+)$','article.views.add_comment'),
                      url(r'^search$','article.views.search_titles'),
                      url(r'^api/',include(article_resource.urls)),
                      url(r'^search_pages/','article.views.search_pages'),
                      url(r'^delete_procedure/','article.views.delete_procedure')
                      # url(r'^add_procedure/(?P<article_id>\d+)$','article.views.add_procedure')
                      )