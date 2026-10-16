import secrets
import string
password=""
letters=string.ascii_letters
#numbers=string.digits
symbols=string.punctuation
secrets.choice(letters)
pass_length=int(input("Enter the length of password:"))
while pass_length > 0:
    password +=(secrets.choice(letters))
    pass_length-=1
    if pass_length<=0:
        break
    password +=str((secrets.randbelow(10)))
    pass_length-=1
    if pass_length<=0:
        break
    password +=(secrets.choice(symbols))
    pass_length-=1
print(password)
# final_string = "".join(str(item) for item in password)
# print(final_string)
