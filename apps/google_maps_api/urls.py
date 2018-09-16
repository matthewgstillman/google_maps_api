from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^enter_trip$', views.enter_trip, name="enter_trip"),
    url(r'^new_trip$', views.new_trip, name="new_trip"),
]