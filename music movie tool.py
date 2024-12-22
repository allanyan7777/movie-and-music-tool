# 定義初始電影和音樂分類字典
movie_categories = {
    "動作": {"瘋狂麥斯：憤怒道": 5, "虎膽龍威": 4},
    "喜劇": {"惡搞之家": 3, "醉後大丈夫": 4},
    "劇情": {"教父": 5, "阿甘正傳": 5},
}

music_categories = {
    "流行": {"Bad Guy - Billie Eilish": 4, "Shape of You - Ed Sheeran": 5},
    "搖滾": {"波希米亞狂想曲 - 皇后樂隊": 5, "酒店加州 - 老鷹樂隊": 4},
}

# 定義最愛字典
favorite_movies = []
favorite_music = []

# 最近看過的電影和音樂記錄
recent_movies = []
recent_music = []

# 修改主選單，加入用戶管理和評論功能
def user_main_menu():
    print("\n用戶管理系統")
    print("1. 登錄")
    print("2. 註冊")

# 音樂或電影主選單函數
def main_selection_menu():
    print("\n歡迎使用分類管理系統")
    print("1. 管理電影")
    print("2. 管理音樂")
    print("3. 登出")
    selection = input("請選擇類型 (1/2/3): ")
    return selection

# 主選單函數
def main_menu():
    print("\n分類管理")
    print("1. 查看所有分類及條目")
    print("2. 添加新的分類")
    print("3. 添加條目到分類")
    print("4. 刪除條目")
    print("5. 用戶輸入查詢條目")
    print("6. 查看最近的條目並新增記錄")
    print("7. 查看我的最愛")
    print("8. 添加到我的最愛")
    print("9. 查看並修改評分")
    print("10. 返回主類型選單")
    print("11.添加評論")
    print("12.查看評論")
    choice = input("請選擇操作: ")
    return choice

# 查看最愛項目
def view_favorites(favorites, category_type):
    if not favorites:
        print(f"\n目前沒有最愛的{category_type}。")
    else:
        print(f"\n我的最愛 {category_type}:")
        for item in favorites:
            print(f"  - {item}")

# 添加項目到最愛
def add_to_favorites(favorites, category_type, categories):
    item = input(f"\n輸入要添加到最愛的{category_type}名稱: ")
    # 檢查該項目是否在相應的分類中
    item_found = False
    for category, items in categories.items():
        if item in items:
            item_found = True
            break

    if item_found:
        if item not in favorites:
            favorites.append(item)
            print(f"成功將{category_type} '{item}' 添加到我的最愛！")
        else:
            print(f"'{item}' 已經是你的最愛了！")
    else:
        print(f"'{item}' 不是有效的{category_type}項目，請先檢查分類。")

# 查看分類及條目
def view_categories(categories, category_type):
    if not categories:
        print(f"\n目前沒有任何{category_type}分類。")
    else:
        for category, items in categories.items():
            print(f"\n分類: {category}")
            for item, rating in items.items():
                print(f"  - {item} (評分: {rating} 顆星)")

# 添加新的分類
def add_category(categories, category_type):
    category = input(f"\n輸入新的{category_type}分類名稱: ")
    if category in categories:
        print("該分類已存在！")
    else:
        categories[category] = {}
        print(f"成功添加{category_type}分類: {category}")

# 添加條目到分類
def add_item_to_category(categories, category_type):
    category = input(f"\n輸入{category_type}的分類: ")
    if category not in categories:
        print(f"該分類不存在！請先添加{category_type}分類。")
    else:
        item = input(f"輸入{category_type}名稱: ")
        if item in categories[category]:
            print(f"該{category_type}已在此分類中！")
        else:
            categories[category][item] = 0  # 初始評分為0
            print(f"成功將{category_type} '{item}' 添加到分類 '{category}' 中。")

# 刪除條目
def delete_item(categories, category_type):
    category = input(f"\n輸入要刪除{category_type}的分類: ")
    if category not in categories:
        print(f"該分類不存在！")
    else:
        item = input(f"輸入要刪除的{category_type}名稱: ")
        if item in categories[category]:
            del categories[category][item]
            print(f"成功刪除{category_type} '{item}'。")
            if not categories[category]:  # 如果分類空了，可以選擇刪除該分類
                delete_empty = input(f"分類 '{category}' 已空，是否刪除該分類？(y/n): ").lower()
                if delete_empty == 'y':
                    del categories[category]
                    print(f"成功刪除分類 '{category}'。")
        else:
            print(f"該{category_type}不在此分類中！")

# 用戶輸入查詢
def search_item(categories, category_type):
    query = input(f"\n輸入想查詢的{category_type}名稱: ").lower()
    found = False
    print("\n搜尋結果:")

    for category, items in categories.items():
        for item, rating in items.items():
            if query in item.lower():
                print(f"{category_type}: '{item}' (分類: {category}, 評分: {rating} 顆星)")
                found = True

    if not found:
        print(f"未找到相關{category_type}。")

# 查看和新增最近看過的條目
def manage_recent_items(recent_items, category_type):
    print(f"\n您最近記錄的{category_type}:")
    if not recent_items:
        print("目前沒有記錄。")
    else:
        for i, item in enumerate(recent_items, start=1):
            print(f"{i}. {item}")

    new_item = input(f"\n輸入您最近記錄的{category_type}名稱(或按 Enter 跳過): ")
    if new_item:
        recent_items.append(new_item)
        print(f"成功添加{category_type}: {new_item}")

# 查看並修改評分
def rate_item(categories, category_type):
    item = input(f"\n輸入您想評分的{category_type}名稱: ")
    found = False
    for category, items in categories.items():
        if item in items:
            found = True
            rating = int(input(f"請為 '{item}' 打分（1到5顆星）: "))
            if 1 <= rating <= 5:
                categories[category][item] = rating
                print(f"成功將 '{item}' 的評分設為 {rating} 顆星！")
            else:
                print("無效的評分，請輸入1到5之間的數字。")
            break

    if not found:
        print(f"未找到名為 '{item}' 的{category_type}。")
# 用戶數據存儲 (假設用戶名和密碼是硬編碼的，可以在現實中使用數據庫來存儲)
users = {
    "user1": {"password": "password1", "favorites_movies": [], "favorites_music": [], "comments": {}},
    "user2": {"password": "password2", "favorites_movies": [], "favorites_music": [], "comments": {}}
}

# 當前登錄的用戶
current_user = None

# 用戶註冊
def register_user():
    username = input("輸入用戶名: ")
    if username in users:
        print("該用戶名已經存在！")
    else:
        password = input("輸入密碼: ")
        users[username] = {"password": password, "favorites_movies": [], "favorites_music": [], "comments": {}}
        print(f"註冊成功，歡迎 {username}！")

# 用戶登錄
def login_user():
    global current_user
    username = input("輸入用戶名: ")
    if username not in users:
        print("該用戶不存在！")
        return None

    password = input("輸入密碼: ")
    if users[username]["password"] == password:
        current_user = username
        print(f"歡迎登錄，{username}！")
    else:
        print("密碼錯誤！")
        return None
    return username

# 用戶登出
def logout_user():
    global current_user
    if current_user:
        print(f"{current_user} 已登出。")
        current_user = None
    else:
        print("未登錄，用戶無法登出。")

# 添加評論功能
def add_comment(categories, category_type):
    if current_user is None:
        print("請先登錄！")
        return

    item = input(f"\n輸入你想評論的{category_type}名稱: ")
    found = False
    for category, items in categories.items():
        if item in items:
            found = True
            comment = input(f"請輸入你對 '{item}' 的評論: ")
            if item not in users[current_user]["comments"]:
                users[current_user]["comments"][item] = []
            users[current_user]["comments"][item].append(comment)
            print(f"成功為 '{item}' 添加評論！")
            break

    if not found:
        print(f"未找到名為 '{item}' 的{category_type}。")

# 查看評論
def view_comments():
    if current_user is None:
        print("請先登錄！")
        return

    print("\n我的評論:")
    if not users[current_user]["comments"]:
        print("您還沒有評論。")
    else:
        for item, comments in users[current_user]["comments"].items():
            print(f"\n{item} 的評論:")
            for i, comment in enumerate(comments, 1):
                print(f"  {i}. {comment}")

# 主程式循環
while True:
    if current_user is None:
        user_main_menu()
        user_choice = input("請選擇操作: ")

        if user_choice == "1":
            login_user()
        elif user_choice == "2":
            register_user()
    else:
    
     selection = main_selection_menu()

     if selection == "1":  # 管理電影
        while True:
            choice = main_menu()
            if choice == "1":
                view_categories(movie_categories, "電影")
            elif choice == "2":
                add_category(movie_categories, "電影")
            elif choice == "3":
                add_item_to_category(movie_categories, "電影")
            elif choice == "4":
                delete_item(movie_categories, "電影")
            elif choice == "5":
                search_item(movie_categories, "電影")
            elif choice == "6":
                manage_recent_items(recent_movies, "電影")
            elif choice == "7":
                view_favorites(favorite_movies, "電影")
            elif choice == "8":
                add_to_favorites(favorite_movies, "電影", movie_categories)
            elif choice == "9":
                rate_item(movie_categories, "電影")
            elif choice == "10":
                break
            elif choice == "11":
                add_comment(movie_categories, "電影")
            elif choice == "12":
                 view_comments()
            else:
                print("無效選擇，請重新輸入。")

     elif selection == "2":  # 管理音樂
        while True:
            choice = main_menu()
            if choice == "1":
                view_categories(music_categories, "音樂")
            elif choice == "2":
                add_category(music_categories, "音樂")
            elif choice == "3":
                add_item_to_category(music_categories, "音樂")
            elif choice == "4":
                delete_item(music_categories, "音樂")
            elif choice == "5":
                search_item(music_categories, "音樂")
            elif choice == "6":
                manage_recent_items(recent_music, "音樂")
            elif choice == "7":
                view_favorites(favorite_music, "音樂")
            elif choice == "8":
                add_to_favorites(favorite_music, "音樂", music_categories)
            elif choice == "9":
                rate_item(music_categories, "音樂")
            elif choice == "10":
                break
            elif choice == "11":
                add_comment(music_categories, "音樂")
            elif choice == "12":
                view_comments()
            else:
                print("無效選擇，請重新輸入。")
     elif selection == "3":
          logout_user()
     else:
        print("無效選擇，請重新輸入。")

       
        
    
        
        

# 主程式循環








