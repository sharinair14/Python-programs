import random as r

num = r.randrange(100)

guess=5

while guess>=0:
    your_no=int(input("\n Enter your number between 1 and 100 "))

    def check(x):
        if your_no == x:
            print('\n You won')
        elif your_no >=x:
            print('\n OOPS,This is not the number.Enter lower no.')
        else:
            print('\n OOPS,This is not the number.Enter higher no')

    if guess > 1:
        check(num)
    elif guess == 1:
        check(num)
        print('\n You have only one chance left')
    else:
        print("\n Sorry !!! You lost")
        break

guess=guess - 1



