#budgeting display functions

def balance(amount):
    length = len(amount)
    n = 0
    while n < length:
        print(amount[n], ': ', amount[n+1], sep='')
        n = n+2

          
