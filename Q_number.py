
#まずは長さを頭の中で想像してもらう
#結果が５センチ以下(low)２５センチ以上(high)なら煽る文章
low = 1
high = 30
'''name_userは遊ぶ人の名前
penis_correct最終的な予想センチ'''

name_user = input('あなたのお名前を教えて下さい')
print(name_user,'さん、ご自身のチンポの長さを頭の中で思い浮かべてください、５回以内に当てます')

#low=highならループを抜けるforループを作る
for penis in range(5):
    if low == high:
        break
    #コンピュータの推測値を確認→推測値はQ_penis
    Q_penis = (low + high) // 2
    print('あなたのチンポは',Q_penis,'より大きいですか？yes/no)')
    answer_penis = input()

    #分岐
    if answer_penis == 'yes':
        low = Q_penis + 1
    else:
        high = Q_penis

print(name_user,'さんのチンポの長さは',low,'センチです！')
if 3 >= low:
    print('大丈夫、大きさが全てではありません')
elif 30 <= low:
    print('嘘はつくものじゃありません')