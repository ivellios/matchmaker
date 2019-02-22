from django.contrib.auth.models import User
from rest_framework import viewsets, status, views, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from games.models import Game
from .serializers import UserSerializer, GameSerializer


class SimpleDemoView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        param = request.GET.get("param")
        return Response({"param": param}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(methods=['GET'], detail=True)
    def score_player_1(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.player1_score += 1
        instance.save(update_fields=['player1_score'])

        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def score_player_2(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.player2_score += 1
        instance.save(update_fields=['player2_score'])

        return Response(status=status.HTTP_200_OK)