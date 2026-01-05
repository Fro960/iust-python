import random

import names

def random_english_name(count = 2):
    return names.get_full_name().split(' ')

print(random_english_name()[0])