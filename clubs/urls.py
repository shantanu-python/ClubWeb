from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='clubs_home_page'),
    url(r'^(?P<slug>[-\w\d]+)/$', views.club_page, name='club_page'),
]
