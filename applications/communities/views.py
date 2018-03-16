from .models import Community
from rest_framework import viewsets
from .serializers import CommunitySerializer

from applications.players.models import Player


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    def perform_create(self, serializer):
        community = serializer.save()
        player = Player.objects.create(name=self.request.user.username)
        community.players.add(player)
