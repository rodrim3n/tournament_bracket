from .models import Player, Team
from django import forms

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
