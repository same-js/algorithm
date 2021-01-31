items = (
    ('もも', 50),
    ('みかん', 100),
    ('ざくろ', 150),
    ('りんご', 200),
    ('ぶどう', 300),
    ('すいか', 400),
)
money = 500
n  = len(items)
count = 0

# 施行回数：2^n つまり 2**n
for i in range(2**n):
    bag = []
    total = 0
    # シフト演算
    for j in range(n):
        if i >> j & 1:
            bag.append(items[j][0])
            total += items[j][1]
    # 判定
    if ( money >= total):
        print('🔵',end='')
        count += 1
    else:
        print('❌',  end='')
    # バッグの中身を出力
    print(' | パターン：{} | 買うもの：{} | 合計金額：{}'.format(i, bag, total))

# 条件に合致するパターン数の出力
print('購入可能なパターンは {} 個ありました'.format(count))
