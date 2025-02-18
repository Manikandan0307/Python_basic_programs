num= int(input("Enter a number: "))
sum_digits =sum(int(digit) for digit in str(num))
print("sum of digits",sum_digits)