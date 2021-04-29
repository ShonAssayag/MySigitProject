cache = dict()
def plus(x, y):
    s = str(x)+str(y)
    if(s in cache.keys()):
        return cache.get(s)
    sum = x + y
    cache.update({s : sum})
    return sum

print(plus(6,7))
print(plus(6,7))