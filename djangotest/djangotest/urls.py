from django.conf.urls import patterns, include, url
from polls.views import login_index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', include('social_auth.urls')),
    url(r'^polls/',include('polls.urls')),
    url(r'^$','polls.views.login_index',name='welcome'),
)
