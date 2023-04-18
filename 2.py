#X=int(input("Введите число x: "))
#Y=int(input("Введите число y: "))
#if X<1 or X>1000 or Y<1 or Y>1000:
    #print("Вы ввели числа непринадлежащие заданному диапазону, повторите еще раз")
#else:
    #P=X+Y
    #S=X*Y
    #flag = 0
    #for i in range (1001):
        #if flag != 1:
            #for j in range (1001):
                #if i+j==P and i*j==S:
                    #print(i,j)
                    #flag=1
            #else:
                #j=1001
    #else:
        #i =1001

S = abs(int(input('Введите первое натуральное число X ')))
P = abs(int(input('Введите второе натуральное число Y ')))
y = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x, y)