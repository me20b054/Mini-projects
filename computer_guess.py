import random 
def computer_guess(x):
    low = 1
    high = x
    feedback = ' '
    while feedback != 'c': 
        guess = random.randint(low,high)
        feedback = input(f"{guess} is hghh(h),low(l) or correct(c) ?") 
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1  
    
    print('yey!computer guessed correctly')

computer_guess(9)