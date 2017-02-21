from appeventos.views import *
from django.conf.urls import include,url
from django.contrib.auth.views import login,logout


urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^orcamento/new/$',orcamento_new,name='orcamento_new'),
    #url(r'^evento/list/$',evento_list,name='evento_list'),

]
