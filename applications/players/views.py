from .models import Player, Team
from rest_framework import viewsets
from .serializers import PlayerSerializer, TeamSerializer
from applications.communities.models import Community  # TODO: ver que onda
from rest_framework.response import Response


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def list(self, request, community_id):
        queryset = Team.objects.filter(community_id=community_id)
        context = {'request': request}
        serializer = TeamSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def perform_create(self, serializer):
        # Validar que los players del team esten en la comunidad
        community_id = self.request.parser_context['kwargs'].get(
            'community_id')

        community = Community.objects.get(pk=community_id)
        serializer.save(community=community)
