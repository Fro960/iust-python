import random

import string

def main():
    length = int(input("Enter length of password: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    get_password(chars, length)
    
    
    
def get_password(chars, length = 12):

    for _ in range(50):
        password = ''
        for i in random.choices(chars, k = length):
            password += i
        print(password)

main()