from models.playermanager import PlayerManage
players = PlayerManage()
while True:
    print(" MENU ".center(50,"="))
    print("1. Hiển thị danh sách cầu thủ")
    print("2. Thêm cầu thủ mới")
    print("3. Cập nhật cầu thủ")
    print("4. Xóa cầu thủ")
    print("5. Tìm kiếm cầu thủ")
    print("6. Thoát")

    user_choice = input("Nhập lựa chọn của bạn (1-6)")
    match user_choice:
        case "1":
            players.show_all()
        case "2":
            players.add_player()
        case "3":
            players.update_player()
        case "4":
            players.delete_player()
        case "5":
            players.search_player()
        case "6":
            print("Thoát")
            break
        case _:
            print("Nhập lại cho đúng lựa chọn (1-6)")
            continue