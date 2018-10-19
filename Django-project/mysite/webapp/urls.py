from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^phaltu/$', views.index, name="index")
]   