from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'mobile', 'address', 'profile_pics']