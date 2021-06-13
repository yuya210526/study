from django.forms import ModelForm
from sample.models import Parent, Child


class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ('name', )
