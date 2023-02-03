currency = int(input('Enter the amount: '))

thousand = 0
five_hundred = 0
two_hundred = 0
hundred = 0
twenty = 0
ten = 0
five = 0
two = 0
one = 0

while currency != 0:
    if currency >= 1000:
        thousand = currency // 1000
        currency = currency % 1000
    elif currency >= 500:
        five_hundred = currency // 500
        currency = currency % 500
    elif currency >= 200:
        two_hundred = currency // 200
        currency = currency % 200
    elif currency >= 100:
        hundred = currency // 100
        currency = currency % 100
    elif currency >= 20:
        twenty = currency // 20
        currency = currency % 20
    elif currency >= 10:
        ten = currency // 10
        currency = currency % 10
    elif currency >= 5:
        five = currency // 5
        currency = currency % 5
    elif currency >= 2:
        two = currency // 2
        currency = currency % 2
    elif currency >= 1:
        one = currency // 1
        currency = currency % 1
    else:
        break

print('\n Printing all the currency')
print('Thousand => ', thousand)
print('Five Hundred => ', five_hundred)
print('Two Hundred => ', two_hundred)
print('Hundred => ', hundred)
print('Twenty => ', twenty)
print('Ten => ', ten)
print('Five => ', five)
print('Two => ', two)
print('One => ', one)




