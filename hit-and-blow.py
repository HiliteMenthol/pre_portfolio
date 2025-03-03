import random

def check_hit_and_blow(secret,guess):
    '''ユーザーの推測値と正解を比較して、ヒットとブローの数を返す'''
   
    #ヒットとブロー変数の初期化
    hit = 0
    blow = 0

    #ヒットのカウント
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            hit += 1
        
    #重複数のカウント
    hit_and_blow = 0
    for num in secret:
        if num in guess:
            hit_and_blow += 1
        
    #ブロー＝重複数からヒット数を引く
    blow = hit_and_blow - hit
    
    
    return hit,blow

    print(secret_numbers) #初めてのおまじない

#開始の説明
print('数当てゲームスタート！')
print('私が１～９の数字を使って私がランダムな数値を作ります')
print('あなたは１桁から９桁の間で行数を指定してください')

#桁数入力
while True:
    n = int(input('何桁の数値でゲームをしますか？（１～９）:'))
    #１～９でループ抜ける
    if 1 <= n <= 9:
        break
print('１～９の数字を入力してください')

#正解の数
numbers = [1,2,3,4,5,6,7,8,9]
secret_numbers = random.sample(numbers,n)
#print(secret_numbers)

#試行回数を初期化
trial_count = 0

#ユーザーから推測した数字を受け取る
while True:
    guess_number = input(f'{n}桁の数字を入力してください')

    #入力された数値をリストに変換
    guess_list = []
    for char in guess_number:
        guess_list.append(int(char))
    print(guess_list)
    
    #試行回数をカウントアップ
    trial_count += 1
    print(f'{trial_count}回目の回答です')
    
    #ユーザの推測値と正解を比較し、ヒット数とブロー数を返す
    hit,blow = check_hit_and_blow(secret_numbers,guess_list)
    
    #結果表示
    if hit == n:
        print(f'正解！ゲームクリアです。正解＝{secret_numbers}')
        print(f'{trial_count}回で正解しました')
        break
    else:
        print(f'ヒット{hit},ブロー{blow}')