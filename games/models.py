from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name='games_created', on_delete=models.CASCADE)
    player1 = models.CharField('Player 1 name', max_length=30)
    player2 = models.CharField('Player 2 name', max_length=30)
    player1_score = models.IntegerField('Player 1 score', default=0)
    player2_score = models.IntegerField('Player 2 score', default=0)

    def __str__(self):
        return f'Game by {self.creator} created at {self.created}'
