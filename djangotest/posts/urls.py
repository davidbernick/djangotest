from django.conf.urls import patterns, include, url
from django.contrib.auth import views

urlpatterns = patterns(
                       'posts.views',
                       url(r'^logout/$', views.logout, {'next_page':'/posts/'},name='logout'),
                       url(r'^$', 'posts_index', {'template_name':'signin.html'}, name='polls_index'),
)
