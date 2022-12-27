#Password generator
import random
print("Welcome to your password generator!")
nr_letters=int(input("Enter the number of letters:"))
nr_symbols=int(input("How many symbols? "))
nr_digits=int(input("How many digits?"))
password=''
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="!@#$%^&*()?~"

for char in range(1, nr_letters+1):
    password+=random.choice(letters)
for char in range(1,nr_digits+1):
    password+=random.choice(numbers)
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)

password_list=list(password) 
random.shuffle(password_list)
finalpassword=''.join(password_list)

print(f"Your password is:{finalpassword}")

