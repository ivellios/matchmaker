from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from games.models import Game
from .serializers import UserSerializer, GameSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
