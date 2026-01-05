def vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

string = input("Enter some text: ").lower()
print(f"Vowels in this string are {vowels(string)}")