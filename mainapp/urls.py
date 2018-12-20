from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^work_list/$', views.work_list, name='work_list'),
    # url(r'^work/(?P<pk>\d+)/$', views.work_detail, name='work_detail'),
    # url(r'^work/new/$', views.work_new, name='work_new'),
    # url(r'^work/(?P<pk>\d+)/edit/$', views.work_edit, name='work_edit'),


    url(r'^device_list/$', views.device_list, name='device_list'),
    url(r'^$', views.device_list, name='device_list'),
    url(r'^device/new/$', views.device_new, name='device_new'),
    url(r'^device/(?P<pk>\d+)/edit/$', views.device_edit, name='device_edit'),
    url(r'^device/(?P<pk>\d+)/remove/$', views.device_remove, name='device_remove'),
    url(r'^device/(?P<pk>\d+)/$', views.device_detail, name='device_detail'),
    url(r'^device/(?P<devicepk>\d+)/work/new/$', views.device_work_new, name='device_work_new'),
    url(r'^device/(?P<devicepk>\d+)/work/(?P<pk>\d+)/edit/$', views.device_work_edit, name='device_work_edit'),
    url(r'^device/(?P<devicepk>\d+)/work/(?P<pk>\d+)/remove/$', views.device_work_remove, name='device_work_remove'),
]
