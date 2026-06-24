

def show_all_func(players):
    print("BẢNG CẦU THỦ".center(100,"="))
    print(f"{'ID':<10} | {'Name':<20} | {'Speed':<10} | {'Technique':<10} | {'Goals':<10} | {'AVG Score':<15} | {'Type':<20}")
    for player in players:
        print(f"{player.id:<10} | {player.name:<20} | {player.speed_score:<10} | {player.technique_score:<10} | {player.goal_score:<10} | {player.averange_score:<15} | {player.performance_type:<20}")
    print("="*100)


