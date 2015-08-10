from django.conf.urls import include, url
from django.contrib import admin

from books.views import index, detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^([\d]+)/$', detail),
]
