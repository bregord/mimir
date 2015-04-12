from django.conf.urls import url

from . import views

urlpatterns = [
       url(r'^$', views.index, name='index'),
       url(r'^register/', views.register, name='register'),
       url(r'^login/',views.our_login,name='our_login')
]
