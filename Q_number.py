
#まずは数字を頭の中で想像してもらう
low = 1
high = 30
'''name_userは遊ぶ人の名前
最終的な予想数字'''

name_user = input('あなたのお名前を教えて下さい')
print(name_user,'さん、頭の中で数字を思い浮かべてください、５回以内に当てます')

#low=highならループを抜けるforループを作る
for number in range(5):
    if low == high:
        break
    #コンピュータの推測値を確認→推測値は
    Q_number = (low + high) // 2
    print('あなたの思い浮かべた数字は',Q_number,'より大きいですか？yes/no)')
    answer_number = input()

    #分岐
    if answer_number == 'yes':
        low = Q_number + 1
    else:
        high = Q_number

print(name_user,'さんの思い浮かべた数字は',low,'です！')