k=int(input())

def f(k):
    if k==0:
        return 1
    else:
        return k*f(k-1)

print(f(k))