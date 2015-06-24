from django.contrib import admin
from part_finder.models import Experiment,Participant,Researcher


class ExperimentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Participant)
admin.site.register(Researcher)


