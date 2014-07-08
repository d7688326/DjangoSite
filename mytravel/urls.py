from django.conf.urls import patterns, include, url
from django.contrib import admin
from article import views as home
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.articles),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/',include('polls.urls',namespace="polls")),
    url(r'^article/',include('article.urls',namespace="articles")),
    url(r'^accounts/',include('userprofile.urls')),
    # user auth
    url(r'^accounts/login/$','mytravel.views.login'),
    url(r'^accounts/auth/$','mytravel.views.auth_view'),
    url(r'^accounts/logout/$','mytravel.views.logout'),
    url(r'^accounts/loggedin/$','mytravel.views.loggedin'),
    url(r'^accounts/invalid/$','mytravel.views.invalid_login'),
    #registration
    url(r'^accounts/register/$','mytravel.views.register_user'),
    url(r'^accounts/register_success/$','mytravel.views.register_success'),


)

if settings.DEBUG:
    urlpatterns+= patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root':settings.MEDIA_ROOT}),
    )