from feature.feature_2 import check_score

def update_player_func(players):
    while True:
        try:
            id = int(input("Nhập ID: "))
        except ValueError:
            print("Sai Dữ liệu nhập lại đi")
            continue

        for player in players:
            if id == player.id:
                try: 
                    speed = int(input("Nhập điểm tốc độ"))
                except ValueError:
                    print("Giá trị lỗi")
                    continue
                speed_check = check_score(speed)
                if speed_check is None:
                    continue
                try: 
                    skill = int(input("Nhập điểm skill"))
                except ValueError:
                    print("Giá trị lỗi")
                    continue
                skill_check = check_score(skill)
                if skill_check is None:
                    continue
                try: 
                    score_skill = int(input("Nhập điểm ghi bàn"))
                except ValueError:
                    print("Giá trị lỗi")
                    continue
                score_check = check_score(score_skill)
                if score_check is None:
                    continue
                player.speed_score = speed
                player.technique_score = skill
                player.goal_score = score_skill
                player.averange_score = player.calculate_averange()
                player.performance_type = player.classify_performance()
                print("Cập nhật hoàn tất")
                break
        print("Không có cầu thủ")
        break
