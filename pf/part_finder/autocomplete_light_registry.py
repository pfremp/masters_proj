import autocomplete_light.shortcuts as autocomplete_light
from cities_light.models import Country, Region, City
from part_finder.models import Languages
# from .models import NonAdminAddAnotherModel
import autocomplete_light.shortcuts as al

#countries auto complete
autocomplete_light.register(Country, search_fields=('name', 'name_ascii',),
    autocomplete_js_attributes={'placeholder': 'country name ..'})


class AutocompleteRegion(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'placeholder': 'region name ..'}

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        country_id = self.request.GET.get('country_id', None)

        choices = self.choices.all()
        if q:
            choices = choices.filter(name_ascii__icontains=q)
        if country_id:
            choices = choices.filter(country_id=country_id)

        return self.order_choices(choices)[0:self.limit_choices]


class AutocompleteCity(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'placeholder': 'city name ..'}

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        region_id = self.request.GET.get('region_id', None)

        choices = self.choices.all()
        if q:
            choices = choices.filter(name_ascii__icontains=q)
        if region_id:
            choices = choices.filter(region_id=region_id)

        return self.order_choices(choices)[0:self.limit_choices]

autocomplete_light.register(Region, AutocompleteRegion)
autocomplete_light.register(City, AutocompleteCity)



# autocomplete_light.register(NonAdminAddAnotherModel,
#     add_another_url_name='non_admin_add_another_model_create')



#languages autocomplete
class OsAutocomplete(al.AutocompleteListBase):
    choices = ['English', 'French', 'Spanish', 'German', 'Mandarin', 'Cantonese', 'Italian', 'Portugese']
al.register(OsAutocomplete)
# al.register(OsAutocomplete)




# class LanguageAutocomplete(al.AutocompleteListBase):
#     search_fields = ['language',]
#     choices = [Languages]
#
# autocomplete_light.register(LanguageAutocomplete)



# class LanguageAutocomplete(autocomplete_light.AutocompleteModelBase):
#     search_fields = ['language']
# autocomplete_light.register(Languages, LanguageAutocomplete)



autocomplete_light.register(Languages, search_fields=('language',),)

# class LangAutocomplete(al.AutocompleteListBase):
#     choices = Languages.objects.all()
#
# al.register(LangAutocomplete, search_fields=('lang', 'lang',))


# class OsAutocomplete(al.AutocompleteListBase):
#     choices = ['English', 'French', 'Spanish', 'German', 'Mandarin', 'Cantonese', 'Italian', 'Portugese']





