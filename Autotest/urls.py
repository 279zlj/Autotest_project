from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from websocket import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'auto/', include('auto.urls')),
    url(r'^echo$', v.echo),
    url(r'^send$', v.send),
    url(r'^$', TemplateView.as_view(template_name="index.html")),

]
