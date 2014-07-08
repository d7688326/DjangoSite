__author__ = 'franklin'
from django.conf.urls import patterns, include,url

urlpatterns = patterns('',
               url(r'^edit_profile/$','userprofile.views.user_profile'),
               url(r'^profile/display','userprofile.views.myprofile'),
               url(r'^profile/myworks','userprofile.views.myworks'),
               url(r'^profile/(?P<username>.*)/$','userprofile.views.profile')
)
