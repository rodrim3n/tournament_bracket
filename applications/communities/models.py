from __future__ import unicode_literals

from django.db import models



class Community(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=100, null=False)
    players = models.ManyToManyField('players.Player', related_name='communities')

    def __str__(self):
        return self.name
