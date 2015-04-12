from django.conf.urls import patterns, url, include
from tutorial import views

urlpatterns = patterns('', url(r'^$', views.editorPage, name='editorPage'),
                       url(r'^markdown/', include('django_markdown.urls')),
                       )
