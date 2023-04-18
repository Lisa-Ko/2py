N = int(input("Введите число "))
S=2
flag =0
for i in range (N):
    if flag != 1:
        S=S**i
        if S <= N:
            print(S)
            S=2
        else:
            flag = 1
    else:
        i = N
