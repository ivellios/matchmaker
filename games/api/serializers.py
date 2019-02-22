from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Game


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ('created', 'creator', 'player1', 'player2', 'player1_score', 'player2_score')
