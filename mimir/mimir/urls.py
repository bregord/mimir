from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'mimir.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('registration.urls')),
    url(r'^user/', include('user_profiles.urls')),
<<<<<<< HEAD
    url(r'^editor/', include('tutorial.urls')),
    url(r'^markdown/', include('django_markdown.urls'))
]
=======
    url(r'^forum/',include('forum.urls'))
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 2e2ce20b23fa368a11b2b5f9258551b9d574fb70
