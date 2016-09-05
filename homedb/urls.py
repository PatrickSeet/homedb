from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homedb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', 'homedbapp.views.test', name='test'),
    url(r'^index/$', 'homedbapp.views.index', name='index'),
    url(r'^profile/$', 'homedbapp.views.profile', name='profile'),
    url(r'^property/(?P<property_id>\w+)/edit/$', 'homedbapp.views.edit_property', name='edit_property'),
    url(r'^property/(?P<property_id>\w+)/delete/$', 'homedbapp.views.delete_property', name='delete_property'),
    url(r'^register/$', 'homedbapp.views.register', name='register'),
    url(r'^$', 'homedbapp.views.index', name='index'),
    url(r'^faq/$', 'homedbapp.views.faq', name='faq'),
    url(r'^properties/$', 'homedbapp.views.properties', name='properties'),
    url(r'^property/new/$', 'homedbapp.views.new_property', name='new_property'),
    url(r'^property/(?P<property_id>\w+)/$', 'homedbapp.views.view_property', name='view_property'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/'}, name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)