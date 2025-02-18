n= int(input("enter the number of terms: "))
n1, n2 = 0, 1

print("Fibonacci sequence:")
for i in range(n):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth

