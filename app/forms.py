from django.forms import ModelForm
from .models import Emails

class UserEmailForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Emails
