from django.forms import ModelForm
from .models import Person

class personForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'