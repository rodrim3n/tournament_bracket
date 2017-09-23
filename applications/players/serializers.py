from .models import Player, Team
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    communities = serializers.StringRelatedField(many=True)
    class Meta:
        model = Player
        fields = (
            'communities',
            'name',
        )


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    player_one = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())
    player_two = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all())

    class Meta:
        model = Team
        fields = (
            'name',
            'player_one',
            'player_two',
        )

    def validate_player_one(self, value):
        community = self.context['request'].parser_context['kwargs'].get('community_id')
        if not Player.objects.filter(pk=value.pk, communities__id=community).exists():
            raise serializers.ValidationError("User does not belong to the community given.")
        return value

    def validate_player_two(self, value):
        community = self.context['request'].parser_context['kwargs'].get('community_id')
        if not Player.objects.filter(pk=value.pk, communities__id=community).exists():
            raise serializers.ValidationError("User does not belong to the community given.")
        return value
