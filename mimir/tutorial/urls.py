from django.conf.urls import patterns, url
from tutorial import views

urlpatterns = patterns('', url(r'^editor/', views.editorPage, name='editorPage'),
                       url('^markdown/', include('django_markdown.urls'))
                       )
