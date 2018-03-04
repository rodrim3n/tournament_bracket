from django.conf.urls import url, include
from rest_framework import routers

import applications.communities.views as views


PREFIX = 'api/v1'

router = routers.DefaultRouter()
router.register(r'%s/communities' % PREFIX, views.CommunityViewSet)

urlpatterns = [url(r'^', include(router.urls))]
