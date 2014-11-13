from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'stories.views.index', name='index'),
    url(r'^story/$', 'stories.views.story', name='story'),
    url(r'^vote/$', 'stories.views.vote', name='vote'),
)
