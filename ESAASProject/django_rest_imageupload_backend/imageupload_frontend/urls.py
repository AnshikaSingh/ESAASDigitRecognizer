from django.conf.urls import url, include
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='static/index.html', permanent=False), name='index'),
    url(r'^copy', RedirectView.as_view(url='static/copy.py.py', permanent=False), name='copy.py')
]
