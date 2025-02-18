text = input("ener the string:")
vow = "aeiouAEIOU"
count =sum (1 for char in text if char in vow)
print("number of vowels:",count)