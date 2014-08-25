from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dragonAgeSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('dragonAgeSite.reference.urls')),
    url(r'^reference/', include('dragonAgeSite.reference.urls')),
    url(r'^post/', include('dragonAgeSite.blog.urls')),
)
