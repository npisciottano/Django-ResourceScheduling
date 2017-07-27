from django.contrib import admin
from Schedule.models import resource, engagement, assignment, client

class resourceAdmin(admin.ModelAdmin):
    model = resource
    list_display = ('resourceID','resource_name','resource_level','resource_firm','resource_group')

class engagementAdmin(admin.ModelAdmin):
    model = engagement
    list_display = ('engagementID','clientID','engagement_description','engagement_code')

class assignmentAdmin(admin.ModelAdmin):
    model = resource
    list_display = ('assignment_week','assignment_resource','assignment_engagement','assignment_hours')

class clientAdmin(admin.ModelAdmin):
    model = client
    list_display = ('clientID','client_name','client_industry','client_location')


# Register your models here.
admin.site.register(resource, resourceAdmin)
admin.site.register(engagement, engagementAdmin)
admin.site.register(assignment, assignmentAdmin)
admin.site.register(client, clientAdmin)