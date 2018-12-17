def h(x1,x2):
    w1 = 20
    w2 = 50
    b = -1000
    a = w1*x1 + w2*x2 + b
    if(a>=0):
        return 1
    else:
        return 0

print(h(x1=20,x2=10)) # ได้ 0
print(h(x1=14,x2=15)) # ได้ 1