from django.conf.urls import patterns, url, include

urlpatterns = patterns(

    '',

    url(r'^$', 'core.views.index', name="index"),

)
