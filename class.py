print('enter dan for gugudan(2~9)')
dan = input('dan:')
count = 1
while True:
    print(''+dan+'*'+str(count)+'='+str(int(dan)*count))
    count += 1
    if count > 9:
        break
