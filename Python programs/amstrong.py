num = int(input("enter a number: "))
order = len(str(num))
sum_digits = sum(int(digit) ** order for digit in str(num))
if num == sum_digits:
    print("Armstrong")

else:
    print("Not an Armstrong")