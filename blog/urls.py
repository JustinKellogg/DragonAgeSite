#from django.conf.urls.defaults import patterns, url
from .views import PostListView, PostDetailView
from .api_views import PostList, PostDetail
from django.conf.urls import patterns, url
from mongogeneric import ListView, DetailView
#from rest_framework.urlpatterns import format_suffix_patterns

from .models import Post


urlpatterns = patterns('',

    url(r'^api/post/$', PostList.as_view(), name='api_post_list'),
    url(r'^api/post/(?P<slug>[\w-]+)/$', PostDetail.as_view(), name='api_post_detail'),
#    url(r'^api/post/(?P<pk>[a-z\d]+)/$', PostDetail.as_view(), name='api_post_detail'),

    url(r'^post/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^$', PostListView.as_view(), name='post_list'),
)

#urlpatterns = format_suffix_patterns(urlpatterns)
