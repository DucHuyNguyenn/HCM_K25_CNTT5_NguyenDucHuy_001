def check_id(id:int):
        if id is None:
               print("Không được để id rỗng")
               return None
        if id < 0 or id > 999:
               print("id từ 1 - 999")
               return None
        return id
def delete_player_func(players):
    while True:
        try:
            id = int(input("Nhập mã cầu thủ"))
        except ValueError:
              print("Lỗi kiểu dữ liệu")
              continue
        id_check = check_id(id)
        if id_check is None:
              continue
        for player in players:
              if id == player.id:
                    print("Bạn có muốn xóa cầu thủ không (Y/N)")
                    while True:
                        user_choice = input("Nhập lựa chọn Y hoặc N").strip().upper()
                        match user_choice:
                            case "Y":
                                    players.remove(player)
                                    print("Xóa thành công")
                                    break
                            case "N":
                                    print("Không xóa")
                                    break
                            case _:
                                print("Nhập lại")
                                continue
        print("Không tìm thấy cầu thủ")
        break
    return
                                    



        
        