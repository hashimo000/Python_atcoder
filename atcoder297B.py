S = list(input())
B=[]
K_R=[]

answer="Yes"

for i in range(8):
    if S[i]== "R" or S[i] == "K":
        K_R.append(S[i])
    elif S[i]=="B":
        B.append(i)

if K_R[0] != K_R[2] :
    answer="No"

elif (B[0]+B[1])%2==0:
    answer="No"

print(answer)