from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import reverse


urlpatterns = [
    url(r'^about/',views.about, name='aboutpage'),
    url(r'^remove/(?P<task_id>.+)/$',views.remove ,name='remove'),
    url(r'^cross_off/(?P<task_id>.+)/$',views.cross_off ,name='cross_off'),
    url(r'^uncross/(?P<task_id>.+)/$',views.uncross,name='uncross'),
    url(r'^',views.home,name='homepage'),
    
]