from django.contrib.auth import get_user_model
from django.forms import fields, models
from entangled.forms import EntangledModelForm
from main.models import EntityComments

class ProductForm(EntangledModelForm):
    color = fields.RegexField(
        regex=r'^#[0-9a-f]{6}$',
    )

    size = fields.ChoiceField(
        choices=[('s', "small"), ('m', "medium"), ('l', "large"), ('xl', "extra large")],
    )

    tenant = models.ModelChoiceField(
        queryset=get_user_model().objects.filter(is_staff=True),
    )

    class Meta:
        model = EntityComments
        entangled_fields = {'passports': ['color', 'size', 'tenant']}  # fields provided by this form
        #untangled_fields = ['name', 'price']  # these fields are provided by the Product model