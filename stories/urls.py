from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^story/$', "stories.views.story"),
    url(r'^$', "stories.views.index"),
)
