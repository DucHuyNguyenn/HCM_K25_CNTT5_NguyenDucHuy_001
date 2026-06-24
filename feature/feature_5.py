from feature.feature_1 import show_all_func

def search_player_func(players):
    name = input("Nhập tên")
    for player in players:
        if name == players.name:
            player.show_all_func
            break
    print("Không có cầu thủ cần tìm")
    return