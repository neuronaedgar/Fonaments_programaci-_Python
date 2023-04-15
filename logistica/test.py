def generador():
    for i in [1,2,3]:
        yield i

data = generador()

try:
    print(next(data))
    print(next(data))   
    print(next(data))
    print(next(data))
except StopIteration:
    print("Final de items")

print(next(data))
