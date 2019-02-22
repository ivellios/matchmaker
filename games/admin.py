from django.contrib import admin

# Register your models here.
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['creator', 'created', 'player1', 'player2', 'player1_result', 'player2_result']
