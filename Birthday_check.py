
#人間の妊娠期間は大体１０ヶ月
#生でした可能性がある月＝test_m 年＝test_y
#生でした可能性がある初日＝df最終日＝de
check_y = int(input('あなたは西暦何年生まれですか？数字のみ記入してください'))
check_m = int(input('あなたが生まれた月は何月ですか？数字のみで記入してください'))
if 1930 <= check_y <= 2025:
    print('',check_y,'年',check_m,'月生まれなんですね、')
else:
    print('あなたはまだ生まれていないか、相当なボケ老人のようですね')

#記入されたcheck_mから１０を引いて‐の値になるならcheck_yから－１
test_m = check_m - 10
if test_m <= 0:
   test_y = check_y - 1
else:
    test_y = check_y - 0

#西暦、数字を小さい方を採用する関数内と無理かも>いけた

get_m = (check_m - 10 - 1) % 12 + 1


#最終的に出したい文書
print('あなたはだいたい',test_y,'年',get_m,'月に受精し、この世に誕生しました')