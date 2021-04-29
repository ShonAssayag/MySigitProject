cache = dict()
def add6(x, y):
    s = str(x)+str(y)
    if(s in cache.keys()):
        return cache.get(s)
    sum = x + y
    cache.update({s : sum})
    return sum

print(add6(6,7))
print(add6(6,7))