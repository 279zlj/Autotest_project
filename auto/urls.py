from auto import views
from django.conf.urls import *

app_name = 'auto'

urlpatterns = [
    url(r'^begin_test/$', views.begin_test, name='begin_test'),
    url(r'^start_running/$', views.start_running, name='start_running'),
    url(r'^restart_running/$', views.restart_running, name='restart_running'),
    url(r'^change_status/$', views.change_status, name='change_status'),
    url(r'^install_system/$', views.install_system, name='install_system'),
    url(r'^search_system_list/$', views.search_system_list, name='search_system_list'),
    url(r'^search_aging_test/$', views.search_aging_test, name='search_aging_test'),
    url(r'^command/$', views.command, name='command'),
    url(r'^search_test/$', views.search_test, name='search_test'),
    url(r'^search/', views.search_history, name='search_history'),
    url(r'^sendip/', views.sendip, name='sendip'),
]
