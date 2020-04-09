bottle = 100

while bottle > 1:
    bottle = bottle-1
    print(bottle, 'bottles of beer on the wall,', bottle, ' bottles of beer.')
    if bottle - 1 == 0:
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    else:
        print('Take one down and pass it around,',
              bottle-1, 'bottles of beer on the wall.')
print('No more bottles of beer on the wall, no more bottles of beer.')
print('Take it down and pass it around, no more bottles of beer on the wall.')
