from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from part_finder.models import Experiment,Participant,Researcher, UserProfile, Contact, University,TodoList, TimeSlot, Payment_type, Payment, Is_paid, Currency, Application, Languages
from django.contrib.auth.models import User
# from .models import NonAdminAddAnotherModel
import autocomplete_light
from part_finder.forms_search import Requirement


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
admin.site.register(TimeSlot)
admin.site.register(Is_paid)
admin.site.register(Currency)
admin.site.register(Payment_type)
admin.site.register(Payment)
admin.site.register(Application)
admin.site.register(Languages)
admin.site.register(Requirement)



# class NonAdminAddAnotherModelAdmin(admin.ModelAdmin):
#     form = autocomplete_light.modelform_factory(NonAdminAddAnotherModel,
#             fields=('name', 'widgets'))

# admin.site.register(NonAdminAddAnotherModel, NonAdminAddAnotherModelAdmin)
