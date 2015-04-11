from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mimir.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('registration.urls')),
    url(r'^user/', include('user_profiles.urls')),
    url(r'^editor/', include('tutorial.urls')),
    url(r'^markdown/', include('django_markdown.urls'))
]
