N = int(input())
A = list(map(int, input().split()))
z=0
for i in range(N+1):
    if i not in A:
        z=i
        break
print(z)
