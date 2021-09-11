from django import forms
from main.models import BIO
class CustomBIOForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(CustomBIOForm, self).save(commit=False)
        aliases = self.data.getlist("extra_field_aliases")
        low_quality_aliases = self.data.getlist("extra_field_low_quality_aliases")
        alternative_spelling = self.data.getlist("extra_field_alternative_spelling")
        instance.aliases = aliases
        instance.low_quality_aliases = low_quality_aliases
        instance.alternative_spelling = alternative_spelling
        if commit:
            instance.save()
        return instance

    class Meta:
        model = BIO
        fields = "__all__"