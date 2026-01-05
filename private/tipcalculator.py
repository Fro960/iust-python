def main():
    user_input = input("enter str:")
    result = convert(user_input)
    print(result)


def convert(text):
    text = text.replace(":)", "😀")
    return text


main()
