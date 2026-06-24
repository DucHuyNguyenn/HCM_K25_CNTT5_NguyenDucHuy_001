from models.classplayer import ClassPlayer
def check_id(id:int,players):
        if id is None:
               print("Không được để id rỗng")
               return None
        if id < 0 or id > 999:
               print("id từ 1 - 999")
               return None
        for player in players:
                if id == player.id:
                    print("ID trùng rồi nhập lại")
                    return None
        
        return id
def check_name(name:str):
        if name is None:
              print("Không được để tên trống")
              return None
        return name
def check_score(score:int):
        if score > 10 or score < 0:
              print("Điểm từ 0 tới 10 thôi")
              return None
        return score
def add_new_func(players):
    while True:
            try: 
                id = int(input("Nhập mã cầu thủ"))
            except ValueError:
                   print("Giá trị lỗi")
                   continue
            
            id_check = check_id(id,players)
            if id_check is None:
                   continue
            
            name = input("Nhập tên cầu thủ")
            name_check = check_name(name)
            if name_check is None:
                   continue
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
            
            
            new_player = ClassPlayer(id=id,name=name,speed_score=speed,technique_score=skill,goal_score=score_skill)
            players.append(new_player)
            print("Tạo cầu thủ thành công")
            return
            # print("tạo cầu thủ nữa Không")
            # user_choice = input("Y/N").strip().upper()
            #     match user_choice:
            #         case "Y":
            #                 continue
            #         case "N":
            #                 break
            #         case _:
            #                 print("Nhập đúng Y hoặc N")
            #                 continue