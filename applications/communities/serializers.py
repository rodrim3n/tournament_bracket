from .models import Community
from rest_framework import serializers


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.StringRelatedField(many=True)
    teams = serializers.StringRelatedField(many=True)

    class Meta:
        model = Community
        fields = (
            'name',
            'players',
            'teams',
        )

