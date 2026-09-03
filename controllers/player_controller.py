from models.player import Player
from views.player_view import ask_player_info, show_player_added

def add_player(players):
    last_name, first_name, birth_date, chess_id = ask_player_info()
    player = Player(last_name, first_name, birth_date, chess_id)
    players.append(player)
    show_player_added(player)