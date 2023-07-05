from django import forms
from . import models

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('image',)

