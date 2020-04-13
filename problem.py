# 2 암호 맞추기-1
realPw = '12'
print('enter pw(2 disit)')
pw = 0
while pw != realPw:
    pw = input('pw:')
    if pw == realPw:
        print('Correct')
    else:
        print('fail, again')
