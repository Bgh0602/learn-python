# 주사위 게임
'''주사위 번호를 맞출 수 있도록 함. 무한반복을 하고 만약 맞추면 반복을 탈출한다.'''
import random
diceN = random.randint(1, 6)
trial = 1
while True:
    guess = int(input('What is the dice number?(1~6):'))
    if guess != diceN:
        print('again!')
        trial += 1
    if guess == diceN:
        print('correct!')
        print('your trial:', trial)
        break
