from .models import Match
from rest_framework import serializers


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    winner_content_object = serializers.StringRelatedField()
    winner_content_type = serializers.StringRelatedField()
    winner_object_id = serializers.StringRelatedField()
    loser_content_object = serializers.StringRelatedField()
    loser_content_type = serializers.StringRelatedField()
    loser_object_id = serializers.StringRelatedField()

    class Meta:
        model = Match
        fields = (
            'id',
            'winner_content_object',
            'winner_object_id',
            'winner_content_type',
            'winner_goals',
            'loser_content_object',
            'loser_object_id',
            'loser_content_type',
            'loser_goals',
        )
