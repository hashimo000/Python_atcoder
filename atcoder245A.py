N = int(input())
A = list(map(int, input().split()))
Z=0
for i in range(N+1):
    if i not in A:
        Z=i
        break
print(Z)
