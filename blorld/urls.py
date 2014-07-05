from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blorld/', include('blorld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

    #url(r'^$', 'dblog.base_views.home'),
)


urlpatterns += patterns('dblog.blog_views',
    url(r'^$', 'main'),
    url(r'^[\w-]+(\d+)$', 'single_post'),
)