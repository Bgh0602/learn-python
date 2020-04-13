print('My name is Alice. your name?')
myName = input()
realDay = 10
print(myName, '', 'guess my birthday(1~30)')
trial = 0
while trial <= 5:
    trial += 1
    guessDay = int(input('guess:'))
    if guessDay < realDay:
        print('guess a later day')
    if guessDay > realDay:
        print('guess a early day')
    if guessDay == realDay:
        print('correct')
        break
print('my birth day is ', realDay)
