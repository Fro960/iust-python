import random

import names


class Email:
    def __init__(self):
        self.domain_name = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com"]

    def get_name(self, count = 2):
        return names.get_full_name().split(' ')
    
    def get_numbers(self):
        return random.randint(10, 999)
    
    def get_email(self):
        first, second = self.get_name()
        number = self.get_numbers()
        return f"{first.lower()}.{second.lower()}{number}{random.choice(self.domain_name)}"

email1 = Email()
with open("emails.txt", "w") as f:
    for i in range(50):
        f.write(f"{i + 1}. {email1.get_email()}\n") 


  