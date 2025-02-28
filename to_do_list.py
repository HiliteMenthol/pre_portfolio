todo_list = []

while True :
    command = input('操作を入力してください（追加 / 削除 / 表示 / 終了）：')
    
    #新しいタスクを追加する
    if command == '追加' :
        task = input('追加したいタスクを入力してください：')
        todo_list.append(task)
        
    #リストにあるタスクを削除する
    elif command == '削除' :
        task = input('削除したいタスクを追加してください：')
        if task in todo_list :
            todo_list.remove(task)
        else:
            print('タスクが見つかりません')
    
    #現在のTo-Doリストを表示
    elif command == '表示' :
        print('タスクを表示します')
        print(todo_list)
    
    #breakを使ってループを抜ける
    elif command == '終了' :
        print('操作を終了します')
        break
    
    else :
        print('無効な操作です')