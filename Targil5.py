def map(func, list):
    array = []
    for i in list:
        array.append(func(i))
    return array


def multi(num):
    return num*2


print(map(multi, [1, 2, 3]))