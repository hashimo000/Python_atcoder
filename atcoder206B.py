N=int(input())
answer=int()
for i in range(N+1):
    answer += i
    if answer >=N:
        print(i)
        break
    