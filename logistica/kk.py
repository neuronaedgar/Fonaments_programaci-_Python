def f1(a):
    return None

def f2(a):
    return f1(a) * f1(a)

print(1 // 2)

#tp = ('a','b','c')
#tp[1] = tp[1] + tp[0]  

#print(tp)
'''
dd = {"1":"0", "0":"1"}
for x in dd.keys():
    print(dd[x][1], end="")

'''

def fun(i=2, o=3):
    return i * o

print(fun(3))

tp = (1, ) + (1, )
print((tp))
tp = tp + tp
print(len(tp))

print((tp))

a = input()
print(10/a)