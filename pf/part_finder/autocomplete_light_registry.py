import autocomplete_light.shortcuts as autocomplete_light
from cities_light.models import Country, Region, City
from part_finder.models import Languages, University
import autocomplete_light.shortcuts as al

# countries auto complete
autocomplete_light.register(Country, search_fields=('name', 'name_ascii',),
    autocomplete_js_attributes={'placeholder': 'country name ..'})

# Auto complete region - filter by city
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


#languages autocomplete
class OsAutocomplete(al.AutocompleteListBase):
    choices = ['French', 'Spanish', 'German', 'Mandarin', 'Cantonese', 'Italian', 'Portugese']
al.register(OsAutocomplete)




# class LangAutocomplete(al.AutocompleteListBase):
#     choices = ['French', 'Spanish', 'German', 'Mandarin', 'Cantonese', 'Italian', 'Portugese']
# al.register(LangAutocomplete)


autocomplete_light.register(Languages, search_fields=('language',), label="languages")
autocomplete_light.register(University, search_fields=('name',), label="university")




