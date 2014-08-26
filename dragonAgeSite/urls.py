from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dragonAgeSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^madmin/', include(admin.site.urls)),
    url(r'^admin/', include('mongonaut.urls')),
    url(r'^', include('reference.urls')),
    url(r'^reference/', include('reference.urls')),
    url(r'^post/', include('blog.urls')),
)
