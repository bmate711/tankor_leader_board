from rest_framework import viewsets
from . import serializers
from . import models


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.TeamSerializer
    queryset = models.Team.objects.all().order_by('score')
