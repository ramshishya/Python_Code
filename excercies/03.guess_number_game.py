import random

random_number = random.randint(1,10)
print (random_number)
guess_number_limit=5

while guess_number_limit>0:
    print('Guess the number')
    guess_numer=int(input())
    guess_number_limit=guess_number_limit-1
    if guess_numer<random_number:
        print('your number is too low')
    elif guess_numer>random_number:
        print('your number is too hight !')
    else:
        print('you got it right')
        break