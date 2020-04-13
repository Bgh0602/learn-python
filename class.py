while True:
    print('choose dan')
    dan = int(input('dan:'))
    if dan < 1 or dan > 9:
        print('again')
    if 0 < dan and dan < 10:
        break
print(dan, 'dan')
count = 1
while True:
    print(dan, '*', count, '=', dan*count)
    count += 1
    if count > 9:
        break
