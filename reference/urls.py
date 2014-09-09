from django.conf.urls import patterns, url
from .api_views.item_api_views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
    url(r'^api/armor/$', ArmorList.as_view(), name='api_armor_list'),
    url(r'^api/armor/(?P<slug>[\w-]+)/$', ArmorDetail.as_view(), name='api_armor_detail'),
     
    url(r'^api/weapon/$', WeaponList.as_view(), name='api_weapon_list'),
    url(r'^api/weapon/(?P<slug>[\w-]+)/$', WeaponDetail.as_view(), name='api_weapon_detail'), 

    url(r'^api/shield/$', ShieldList.as_view(), name='api_shield_list'),
    url(r'^api/shield/(?P<slug>[\w-]+)/$', ShieldDetail.as_view(), name='api_shiel_detail'),

    url(r'^api/gear/$', GearList.as_view(), name='api_gear_list'),
    url(r'^api/gear/(?P<slug>[\w-]+)/$', GearDetail.as_view(), name='api_gear_detail'),

    url(r'^api/trap/$', TrapList.as_view(), name='api_trap_list'),
    url(r'^api/trap/(?P<slug>[\w-]+)/$', TrapDetail.as_view(), name='api_trap_detail'),

    url(r'^api/poison/$', PoisonList.as_view(), name='api_poison_list'),
    url(r'^api/poison/(?P<slug>[\w-]+)/$', PoisonDetail.as_view(), name='api_poison_detail'),

    url(r'^api/grenade/$', GrenadeList.as_view(), name='api_grenade_list'),
    url(r'^api/grenade/(?P<slug>[\w-]+)/$', GrenadeDetail.as_view(), name='api_grenade_detail'),


)

urlpatterns = format_suffix_patterns(urlpatterns)
