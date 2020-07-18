from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
    url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
    url(r'^create_s/$',views.StudentCreateView.as_view(),name='create_s'),
    url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
    url(r'^update_s/(?P<pk>\d+)/$',views.StudentUpdateView.as_view(),name='update_s'),
    url(r'^delete/(?P<pk>\d+)/$',views.SchoolDeleteView.as_view(),name='delete'),
    url(r'^delete_s/(?P<pk>\d+)/$',views.StudentDeleteView.as_view(),name='delete_s')
]
