from django.conf.urls import url, include
from rest_framework import routers

import applications.players.views as views


PREFIX = 'api/v1'

router = routers.DefaultRouter()
router.register(r'%s/players' % PREFIX, views.PlayerViewSet)
router.register(r'%s/communities/(?P<community_id>[0-9]+)/teams' % PREFIX,
                views.TeamViewSet)

urlpatterns = [url(r'^', include(router.urls))]
