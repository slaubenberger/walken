from walken.views import MovieList, FileList, MovieDetail

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'walken.views.home', name='home'),
    # url(r'^walken/', include('walken.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MovieList.as_view()),
    url(r'^files/', FileList.as_view()),
    url(r'^movies/(?P<pk>\w+)/', MovieDetail.as_view()),

)
