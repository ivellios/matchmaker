import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, status, views, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from games.models import Game
from .serializers import UserSerializer, GameSerializer


class SimpleDemoDjangoView(View):
    def get(self, request):
        param = request.GET.get('param')
        response = json.dumps({"param": param})
        return HttpResponse(response)


class SimpleDemoView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        param = request.GET.get("param")
        return Response({"param": param}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GameViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(methods=['GET'], detail=True)
    def score_player_1(self, request, *args, **kwargs):
        self.get_object().score_1()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def score_player_2(self, request, *args, **kwargs):
        self.get_object().score_2()
        return Response(status=status.HTTP_200_OK)
