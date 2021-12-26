from .models import Setting
from django import forms


# This form has multiple fields for user setting update
class SettingUpdateForm(forms.ModelForm):
    class Meta:
        model = Setting
        exclude = ('user',)
        