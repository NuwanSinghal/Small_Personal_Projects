import sys, time

Num = int(input("Enter a Number to begin the conjecture \n> "))
Nums = []

while Num != 1:
    if Num % 2 == 0:
        Num = Num/2
        Nums.append(Num)
    elif Num % 2 != 0:
        Num = ((Num*3) + 1)
        Nums.append(Num)
    elif Num == 1:
        Nums.append(Num)
        break
    else:
        break
print(Nums)
print(f"This Starting Number led to {len(Nums)} Terms")
