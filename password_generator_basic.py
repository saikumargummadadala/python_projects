import random
alphabets="abcdefghijklmnopqrstuvwxyz"
chars=int(input("number of chars required in your password:"))
number=int(input("no of nums required in your password:"))
symbo=int(input("no of symbols required in your password:"))
letters=[]
for i in range(chars+1):
    if i%2==0:
        alpha_choice=random.choice(alphabets).upper()
        letters.append(alpha_choice)
    else:
         alpha_choice=random.choice(alphabets)
         letters.append(alpha_choice)
nums="0123456789"
numbs=[]
for i in range(number+1):
    nums_choice=random.choice(nums)
    numbs.append(nums_choice)
symbols=r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
symbol=[]
for i in range(symbo+1):
    symbols_choice=random.choice(symbols)
    symbol.append(symbols_choice)
result=letters+numbs+symbol
random.shuffle(result)
result="".join(result)
print(result)