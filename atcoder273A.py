K=int(input())

def f(K):
    if K==0:
        return 1
    else:
        return K*f(K-1)


print(f(K))