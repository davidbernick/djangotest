from django.conf.urls import patterns, include, url

urlpatterns = patterns(
                       'polls.views',
                       url(r'^$', 'login_index', {'template_name':'signin.html'}, name='polls_index'),
)