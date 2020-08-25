from django.shortcuts import render
from game.models import Game, Player, PlayerGameInfo
from game.forms import NumberForm
from time import time


def show_home(request):
    context = {}

    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            game = Game.objects.get(pk=request.session['game_id'])
            player = Player.objects.get(pk=request.session['player_id'])

            if game.author == player:
                game.number = form.cleaned_data['number']
                game.save()
                context['game'] = game
                context['status'] = 'waiting'
            else:
                if game.ended:
                    context['status'] = 'lose'
                    del request.session['game_id']
                else:
                    entered_number = form.cleaned_data['number']
                    current_player_game_info = PlayerGameInfo.objects.get(game=game, player=player)
                    current_player_game_info.attempts += 1
                    current_player_game_info.save()

                    if game.number == entered_number:
                        game.ended = True
                        game.save()
                        del request.session['game_id']
                        context['status'] = 'win'
                        context['comment'] = f'Вы угадали число {entered_number}!'

                    elif game.number > entered_number:
                        context['status'] = 'play'
                        context['form'] = NumberForm()
                        context['comment'] = 'Введенное число меньше угадываемого'

                    elif game.number < entered_number:
                        context['status'] = 'play'
                        context['form'] = NumberForm()
                        context['comment'] = 'Введенное число больше угадываемого'
    else:
        if 'game_id' in request.session:
            game = Game.objects.get(pk=request.session['game_id'])
            player = Player.objects.get(pk=request.session['player_id'])

            if game.author == player:
                context['game'] = game
                context['status'] = 'waiting'

                if game.ended:
                    player = PlayerGameInfo.objects.filter(game=game)
                    context['attempts'] = sum(pl.attempts for pl in player)
                    del request.session['game_id']

            else:
                context['form'] = NumberForm()
                context['status'] = 'play'

        else:
            if 'player_id' not in request.session:
                player = Player.objects.create(id=int(time()))
                request.session['player_id'] = player.id
            else:
                player = Player.objects.get(pk=request.session['player_id'])

            game = Game.objects.filter(ended=False).first()
            if game is None:
                game = Game.objects.create(author=player, ended=False)
                context['form'] = NumberForm()
                context['status'] = 'init'
            else:
                PlayerGameInfo.objects.create(game=game, player=player, attempts=0)
                context['form'] = NumberForm()
                context['status'] = 'play'

            request.session['game_id'] = game.id

    return render(
        request,
        'home.html',
        context
    )
