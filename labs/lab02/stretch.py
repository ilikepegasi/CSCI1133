num = int(input("Enter a 4 digit number: "))
ones = num % 10
print(f"Ones digit is, {ones}")
tens = (num // 10) % 10
print(f"Tens digit is {tens}")
hunds = int((num % 1000) // 100) 
print(f"Hundreds digit is {hunds}")
thous = int(num // 1000)
print(f"Thousands digit is {thous}")
rev = str(ones)+str(tens)+str(hunds)+str(thous)
print(f"Original number reversed is {rev}")
