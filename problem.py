# 2 암호 맞추기-2
import random
realPw = random.randint(11, 20)
print('enter pw(11~20)')
pw = 0
while pw != realPw:
    pw = int(input('pw:'))
    if pw == realPw:
        print('Correct')
    else:
        print('fail, again')
