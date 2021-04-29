def func(id):
    str = id[0:8]
    temp = 1
    sum = 0
    x = 0
    for num in str:
        n = int(num)*temp
        if n > 9:
            n = n % 10 + int(n / 10)
        sum += n
        if temp == 1:
            temp = 2
        else:
            temp = 1

    round_num = sum - sum % 10 + 10

    if round_num - sum == int(id[8]):
        return True
    return False


id = '212694012'
print(func(id))