from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'rescue'
urlpatterns = [


    url(r'^$',
        views.PatientList.as_view(),
        name='patient_list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.PatientDetail.as_view(),
        name='patient_detail'),
    url(r'^create/$',
        views.PatientCreate.as_view(),
        name='patient_create'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        views.PatientUpdate.as_view(),
        name='patient_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.PatientDelete.as_view(),
        name='patient_delete'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]