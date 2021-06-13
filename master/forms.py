from django.forms import ModelForm
from master.models import Parent, Child


class ParentForm(ModelForm):
    class Meta:
        model = Parent
        fields = ('name', )
       
class ChildForm(ModelForm):
    class Meta:
        model = Child
        fields = ('name', ) 
