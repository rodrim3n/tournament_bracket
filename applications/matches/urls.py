from django.conf.urls import url, include
from rest_framework import routers

import applications.matches.views as views


PREFIX = 'api/v1'

router = routers.DefaultRouter()
router.register(r'%s/communities/(?P<community_id>[0-9]+)/matches' % PREFIX,
                views.MatchViewSet)

urlpatterns = [url(r'^', include(router.urls))]
