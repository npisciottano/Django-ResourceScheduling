from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from Schedule import views
from Schedule.views import EngagementList, AssignmentList, ResourceList, ClientList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
    url(r'^engagements/$', EngagementList.as_view()),
    url(r'^assignments/$', AssignmentList.as_view()),
    url(r'^resources/$', ResourceList.as_view()),
    url(r'^clients/$', ClientList.as_view()),
    url(r'^schedule/$', views.schedule, name='schedule'),
    url(r'^resource/add/$', views.ResourceCreate.as_view(success_url='/resources/'), name='resource-add'),
    url(r'^engagement/add/$', views.EngagementCreate.as_view(success_url='/engagements/'), name='engagement-add'),
    url(r'^assignment/add/$', views.AssignmentCreate.as_view(success_url='/assignments/'), name='assignment-add'),
    url(r'^client/add/$', views.ClientCreate.as_view(success_url='/clients/'), name='client-add'),
 ]
