from django import forms
from .models import Match
from applications.players.models import Player, Team
from django.db.models import Q

class MatchForm(forms.ModelForm):
    player_one = forms.ModelChoiceField(queryset=Player.objects.all())
    player_two = forms.ModelChoiceField(queryset=Player.objects.all())

    class Meta:
        model = Match
        fields = '__all__'
