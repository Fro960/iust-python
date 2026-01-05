nums = [1, 2, 34, 78, 99, 45, 23]


def get_max_num(lst):
    max = 0
    for num in lst:
        if num > max:
            max = num

    return max


print(get_max_num(nums))
