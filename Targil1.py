def func1():
    num = '0'
    sum = 0
    while(num != "stop"):
        sum += int(num)
        num = input("enter a number, type stop to end: ")
    print("sum: " + str(sum))


def func2():
    list = input("enter nums: ")
    array = list.split(',')
    sum = 0
    for i in array:
        sum += int(i)

    print("sum: " + str(sum))

func1()
func2()