from django.conf.urls import url

from . import views

urlpatterns = [
       url(r'^(?P<username>[\w|\W-]{1,50})/$', views.profile, name='user')
       url(r'^(?P<title>[\w|W-]{1,50})/$', views.showSeminar, name='title')
]
