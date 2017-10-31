from django.conf.urls import url
from . import views

app_name = 'Blog'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact-me/$', views.contact, name='cantact'),
    url(r'^profileweb/$', views.web, name='web'),
    url(r'^resumeacademic/$', views.academic, name='acdemic'),
    url(r'^research/$', views.research, name='research'),
    url(r'^aboutme/$', views.about, name='aboutme'),
]