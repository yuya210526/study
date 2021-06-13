from django.forms import ModelForm
from plan.models import Plan


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = (
            'plans',
            'results',
            )
