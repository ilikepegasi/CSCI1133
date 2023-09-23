
import platform

vers = platform.python_version()
assert vers[0] == '3', "You must use Python 3, "+vers+" is not acceptable"
print("Python 3 confirmed.")


num_cookies = input("How many cookies do you want to make? ")
num_cookies = int(num_cookies)
recipe_mult = num_cookies/12
butter = str(125*recipe_mult)+"g butter"
sugar = str(225*recipe_mult)+"g sugar"
eggs = str(max(1,round(recipe_mult)))+" eggs"
vanilla = str(recipe_mult)+" tsp vanilla extract"
flour = str(225*recipe_mult)+"g flour"
salt = str(0.5*recipe_mult)+" tsp salt"
chips = str(200*recipe_mult)+"g chocolate chips" 
print(butter)
print(sugar)
print(eggs)
print(vanilla)
print(flour)
print(salt)
print(chips)


amt = float(input("Enter the loan amount in dollars: "))
N = float(input("Enter the loan duration in months: "))
r = (float(input("Enter the % annual interest rate: "))/100)/12
payment = (r*amt)/(1 - (1+r)**(-N))
print("Your monthly payment is: " + str(round(payment,2)))


# Office Hours (leave these lines commented out, this isn't Python code)
# Name of the TA who you visited in office hours: Nathan Taylor
# Above TA's favorite color: Green

