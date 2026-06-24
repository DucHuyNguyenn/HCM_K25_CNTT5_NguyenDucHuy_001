
from feature.feature_1 import  show_all_func
from feature.feature_2 import add_new_func
from feature.feature_3 import update_player_func
from feature.feature_4 import delete_player_func
from feature.feature_5 import search_player_func
class PlayerManage:
    def __init__(self):
        self.players =[]
    def show_all(self):
        show_all_func(self.players)
    def add_player(self):
        add_new_func(self.players)
    def update_player(self):
        update_player_func(self.players)
    def delete_player(self):
        delete_player_func(self.players)
    def search_player(self):
        search_player_func(self.players)