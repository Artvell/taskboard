from django import forms
from main.models import Entity
class CustomEntityForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(CustomEntityForm, self).save(commit=False)
        external_sources = self.data.getlist("extra_field_external_sources")
        locations = self.data.getlist("extra_field_locations")
        instance.external_sources = external_sources
        instance.locations = locations
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Entity
        fields = "__all__"