import names

import random


def main():
    with open("emails.txt", 'w') as email:
        for _ in range(100):
            email.write(f"{get_email()}\n")

def get_name():
    return names.get_full_name().split(" ")

def get_number():
    return random.randint(9, 99)

def get_domain_name():
    domain_names = ["@gmail.com", "@yahoo.com", "@outlook.com", "@iust.ac.in"]
    return random.choice(domain_names)

def get_email():
    first, last = get_name()
    num = get_number()
    domain_name = get_domain_name()
    email = f"{first.lower()}.{last.lower()}{num}{domain_name}" # example "malcolm.x1967@gmail.com"
    return email

main()
