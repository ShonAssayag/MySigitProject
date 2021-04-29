def ex3():
    st = input("input string ")
    count = 1
    output = ''
    for i in range(len(st)-1):
        if st[i] == st[i + 1]:
            count += 1
        else:
            output += st[i] + str(count)
            count = 1

    output += st[len(st)-1] + str(count)
    print(output)

ex3()