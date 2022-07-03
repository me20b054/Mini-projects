import random     
def guess_no(x):
    num = random.randint(1,x)
    guess = 0
    while guess != num :
        guess = int(input('guess a number: '))
        if num > guess:
            print(f"guessed number {guess} is low ")
        elif num < guess:
            print(f"guessed number {guess} is high ")
        else:
            print("yey! you guessed it correctly") 
   
guess_no(10)