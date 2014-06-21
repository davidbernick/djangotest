from django.conf.urls import patterns, include, url
from django.contrib.auth import views

urlpatterns = patterns(
                       'polls.views',
                       url(r'^logout/$', views.logout, {'next_page':'/polls/'},name='logout'),
                       url(r'^$', 'polls_index', {'template_name':'signin.html'}, name='polls_index'),
)
