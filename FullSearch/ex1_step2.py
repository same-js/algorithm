money = 300
items = (
    ('みかん', 100),
    ('りんご', 200),
    ('ぶどう', 300),
)
n = len(items)

for i in range(2**n):
    bag = []

    for j in range(n):
        print('{}({}) >> {} & 1 の結果は {}'.format(i, bin(i), j, (i >> j & 1)), end=" | ")
        if (i >> j) & 1:
            print('bagに{}をappend'.format(items[j][0]), end='')
            bag.append(items[j][0])
        print('')
    print('pattern {}: '.format(i), end='')
    print(bag)
