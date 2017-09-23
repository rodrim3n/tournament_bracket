from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse


class Player(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)

    winner_matches = GenericRelation(
        'matches.Match',
        related_query_name='winner',
        content_type_field='winner_content_type',
        object_id_field='winner_object_id'
    )

    loser_matches = GenericRelation(
        'matches.Match',
        related_query_name='loser',
        content_type_field='loser_content_type',
        object_id_field='loser_object_id'
    )

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50) # TODO: Unique for every community
    player_one = models.ForeignKey(Player, related_name='player_one', on_delete=models.CASCADE)
    player_two = models.ForeignKey(Player, related_name='player_two', on_delete=models.CASCADE)
    community = models.ForeignKey('communities.Community', related_name='teams', on_delete=models.CASCADE)

    winner_matches = GenericRelation(
        'matches.Match',
        related_query_name='winner',
        content_type_field='winner_content_type',
        object_id_field='winner_object_id',
    )

    loser_matches = GenericRelation(
        'matches.Match',
        related_query_name='loser',
        content_type_field='loser_content_type',
        object_id_field='loser_object_id',
    )

    def __str__(self):
        return "{name}: {player} + {player2}".format(
            name=self.name,
            player=self.player_one,
            player2=self.player_two,
        )
