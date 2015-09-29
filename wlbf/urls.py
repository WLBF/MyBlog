from django.conf.urls import patterns, url
from wlbf import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'), 
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_blog/$', views.add_blog, name='add_blog'),
    url(r'^goto/$', views.track_url, name='goto'),
    url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
)
