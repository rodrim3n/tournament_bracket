from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Match(models.Model):
    community = models.ForeignKey(
        'communities.Community',
        related_name='matches',
        on_delete=models.CASCADE,
    )

    winner_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='winner',
        editable=False,
    )
    winner_object_id = models.PositiveIntegerField(editable=False)
    winner_content_object = GenericForeignKey(
        'winner_content_type',
        'winner_object_id',
    )

    loser_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='loser',
        editable=False,
    )
    loser_object_id = models.PositiveIntegerField(editable=False)
    loser_content_object = GenericForeignKey(
        'loser_content_type',
        'loser_object_id',
    )

    winner_goals = models.IntegerField()
    loser_goals = models.IntegerField()

    def match_winner(self):
        return self.winner_content_object

    def match_loser(self):
        return self.loser_content_object
