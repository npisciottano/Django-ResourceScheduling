from django.shortcuts import render
from django.views.generic import ListView
from Schedule.models import engagement, assignment, resource, client
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    return render(request,'index.html')

class EngagementList(ListView):
    model = engagement
    template_name = 'eng_list.html'

class AssignmentList(ListView):
    model = assignment
    template_name = 'assign_list.html'

class ResourceList(ListView):
    model = resource
    template_name = 'resource_list.html'

class ClientList(ListView):
    model = client
    fields = ['client_name', 'client_industry', 'client_location']
    template_name = 'client_list.html'

def schedule(request):
    return render(request, 'schedule.html')

class ResourceCreate(CreateView):
    model = resource
    fields = ['resource_name', 'resource_level', 'resource_firm', 'resource_group']

class EngagementCreate(CreateView):
    model = engagement
    fields = ['clientID', 'engagement_description', 'engagement_code']

class AssignmentCreate(CreateView):
    model = assignment
    fields = ['assignment_week', 'assignment_resource', 'assignment_engagement', 'assignment_hours']

class ClientCreate(CreateView):
    model = client
    fields = ['client_name', 'client_industry', 'client_location']

class ClientEdit(UpdateView):
    model = client
    fields = ['client_name', 'client_industry', 'client_location']
    template_name_suffix = '_update_form'


#Building client+engagement view
#https://stackoverflow.com/questions/12187751/django-pass-multiple-models-to-one-template