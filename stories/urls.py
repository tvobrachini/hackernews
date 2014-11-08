from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^story/$', "stories.views.story"),
    url(r'^$', "stories.views.index"),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'auth/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}),
)
