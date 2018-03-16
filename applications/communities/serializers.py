from .models import Community
from rest_framework import serializers


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.StringRelatedField(many=True, read_only=True)
    teams = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Community
        fields = (
            'name',
            'players',
            'teams',
        )
