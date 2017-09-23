"""tournament_bracket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from applications.matches import views as matches_views
from applications.players import views as players_views
from applications.communities import views as communities_views

router = routers.DefaultRouter()
router.register(r'players', players_views.PlayerViewSet)
router.register(r'communities', communities_views.CommunityViewSet)
router.register(r'communities/(?P<community_id>[0-9]+)/teams', players_views.TeamViewSet)
router.register(r'communities/(?P<community_id>[0-9]+)/matches', matches_views.MatchViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
