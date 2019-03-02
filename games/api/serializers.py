from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Game


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


class GameSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    player1_score = serializers.IntegerField(read_only=True)
    player2_score = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = ('id', 'created', 'creator',
                  'player1', 'player2',
                  'player1_score', 'player2_score')
