from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.Album_View.as_view(), name = "album"),
    url(r'^artist/(?P<pk>[0-9]+)/$', views.Artist_View.as_view(), name="artist"),

]