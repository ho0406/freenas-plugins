from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/headphones/(?P<plugin_id>\d+)/', include('headphonesUI.freenas.urls')),
)
