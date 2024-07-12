from django import forms

from .models import TravelPost


class TravelPostForm(forms.ModelForm):
    class Meta:
        model = TravelPost
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
