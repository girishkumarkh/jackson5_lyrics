from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'jackson.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^homepage', 'lyrics.views.homepage', name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)