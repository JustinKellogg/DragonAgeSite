from django.conf.urls import patterns, url
from .api_views.item_api_views import ArmorList, ArmorDetail
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    url(r'^api/armor/$', ArmorList.as_view(), name='api_armor_list'),
    url(r'^api/armor/(?P<slug>[\w-]+)/$', ArmorDetail.as_view(), name='api_armor_detail'),
     
)

urlpatterns = format_suffix_patterns(urlpatterns)
