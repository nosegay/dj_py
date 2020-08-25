from django.db import models


class Player(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'player'


class Game(models.Model):
    author = models.ForeignKey(Player, related_name='started_game', on_delete=models.DO_NOTHING)
    number = models.IntegerField(null=True)
    players = models.ManyToManyField(Player, related_name='game', through='PlayerGameInfo')
    ended = models.BooleanField()

    class Meta:
        db_table = 'game'


class PlayerGameInfo(models.Model):
    game = models.ForeignKey(Game, related_name='player_game_info', on_delete=models.DO_NOTHING)
    attempts = models.IntegerField()
    player = models.ForeignKey(Player, related_name='player_game_info', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'player_game_info'
