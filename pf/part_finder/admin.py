from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from part_finder.models import Experiment,Participant,Researcher, UserProfile, Contact, University, Locations, Dummy
from django.contrib.auth.models import User

class ExperimentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}






# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Participant)

admin.site.register(UserProfile)
admin.site.register(Researcher)
admin.site.register(Contact)
admin.site.register(University)
admin.site.register(Locations)
admin.site.register(Dummy)


