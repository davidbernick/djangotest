from django.conf.urls import patterns, include, url
from django.contrib.auth import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TaskList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskList)

urlpatterns = patterns(
                       'posts.views',
                       url(r'^logout/$', views.logout, {'next_page':'/posts/'},name='logout'),
                       url(r'^$', 'posts_index', {'template_name':'signin.html'}, name='posts_index'),
                       url(r'^api/', include(router.urls)),
                       #url(r'^tasksapi/(?P<pk>[0-9]+)$', 'tasks_detail'),
)

