from rest_framework import viewsets
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Match
from .serializers import MatchSerializer
import applications.players.models as content_models


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def perform_create(self, serializer):
        winner_object_id = self.request.data['winner_object_id']
        winner_content_type = self.request.data['winner_content_type']
        loser_object_id = self.request.data['loser_object_id']
        loser_content_type = self.request.data['loser_content_type']
        community = self.kwargs['community_id']

        try:
            winner_content_object_class = getattr(
                content_models,
                winner_content_type.capitalize()
            )
            winner = winner_content_object_class.objects.get(
                pk=winner_object_id,
                communities__id=community,
            )
        except (ObjectDoesNotExist, NameError):
            raise Http404

        try:
            loser_content_object_class = getattr(
                content_models,
                loser_content_type.capitalize()
            )
            loser = loser_content_object_class.objects.get(
                pk=loser_object_id,
                communities__id=community,
            )
        except (ObjectDoesNotExist, NameError):
            raise Http404

        serializer.save(
            community_id=community,
            winner_content_object=winner,
            loser_content_object=loser,
        )

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        qs.filter(community_id=self.kwargs.get('community_id'))
        return qs
