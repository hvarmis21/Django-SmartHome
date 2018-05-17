from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^detail/$', detail_view, name="detail"),
    url(r'^form/$', user_form, name="form"),

]