from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^howstr/$', views.howstr_home, name='howstr_home'),
    url(r'^howstr/checkbox/(yes|no|what)/(.*)$', views.howstr_checkbox, name='howstr_checkbox'),
] 

#if settings.DEBUG:
#    urlpatterns += url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})

from django.conf.urls.static import  static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)