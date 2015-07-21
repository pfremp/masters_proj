from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from part_finder.models import Experiment,Participant,Researcher, UserProfile, Contact, University,TodoList, TodoItem
from django.contrib.auth.models import User
# from .models import NonAdminAddAnotherModel
import autocomplete_light


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
admin.site.register(TodoList)
admin.site.register(TodoItem)



# class NonAdminAddAnotherModelAdmin(admin.ModelAdmin):
#     form = autocomplete_light.modelform_factory(NonAdminAddAnotherModel,
#             fields=('name', 'widgets'))

# admin.site.register(NonAdminAddAnotherModel, NonAdminAddAnotherModelAdmin)
