from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^control/$', ControlList.as_view(), name='control-list'),
    url(r'^control/(?P<pk>[0-9]+)/$', ControlDetail.as_view(), name='control-detail'),
    url(r'control/export', export_controls),
    url(r'control/import', import_controls)
]
