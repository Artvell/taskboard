from django import forms
from main.models import EntityComments
from main.functions.tableDataToJson import tableDataToJson
class CustomEntityCommentsForm(forms.ModelForm):
    #extra_field = forms.CharField(widget=forms.Textarea,required=False)
    def save(self, commit=True):
        instance = super(CustomEntityCommentsForm, self).save(commit=False)
        pass_ids = self.data.getlist("passports_id")
        pass_fields = self.data.getlist("extra_field_passports")
        pass_keys = self.data.getlist("external_sources_passports")
        pass_counters = self.data.getlist("passports_counters")
        keywords_ids = self.data.getlist("keywords_id")
        keywords_fields = self.data.getlist("extra_field_keywords")
        keywords_keys = self.data.getlist("external_sources_keywords")
        keywords_counters = self.data.getlist("keywords_counters")
        countries_ids = self.data.getlist("countries_id")
        countries_fields = self.data.getlist("extra_field_countries")
        countries_keys = self.data.getlist("external_sources_countries")
        countries_counters = self.data.getlist("countries_counters")
        instance.passports = tableDataToJson(pass_ids,pass_fields,pass_keys,pass_counters)
        instance.keywords = tableDataToJson(keywords_ids,keywords_fields,keywords_keys,keywords_counters)
        instance.countries = tableDataToJson(countries_ids,countries_fields,countries_keys,countries_counters)
        if commit:
            instance.save()
        return instance
        
    class Meta:
        model = EntityComments
        fields = "__all__"