Salary=input("What is your salary?")
Housing=input("What is your housing?")
Bills=input("How much do you spend on  your bills?")
Food=input("Haw much do you spend on your food?")
Travel=input("How much do you spend on travel?")

def isnumeric(s):
    if s == str("0,1,2,3,4,5,6,7,8,9" or "."):
         print("it is valid")
    
if isnumeric(Salary) and isnumeric(Housing) and isnumeric(Bills) and isnumeric(Food) and isnumeric(Travel):
    print("invalid input,please try again")
else:
    print("All inputs confirmed valid")
Salary  = float(Salary)
Housing = float(Housing)
Bills   = float(Bills)
Food    = float(Food)
Travel  = float(Travel)

Tax=0
if Salary <= 10000:
    tax = round(Salary * 0.05, 2)
elif Salary <= 40000:
    tax = round(Salary * 0.1, 2)
elif Salary <= 80000:
    tax = round(Salary * 0.15, 2)
else:
    tax = round(Salary * 0.20, 2)
    
Housing = Housing * 12
Bills = Bills * 12
Food = Food * 52
Travel = Travel

extra = Salary - Housing - Bills - Food - Travel - Tax
Housing = 24.0
Bills = 8.4
Food = 5.2
Travel = 5.0
Tax= 20.0
extra = 37.4
print("-----------------------------------------------------------------------")
print("Housing | $" , format(Housing, '11,.2f') , " | " , format(Housing, '5,.1f')  , '% | ' , ('#' * int(Housing)))
print("Bills | $" , format(Bills, '11,.2f') , " | " , format(Bills, '5,.1f')  , '% | ' , ('#' * int(Bills)))
print("Food | $" , format(Food, '11,.2f') , " | " , format(Food, '5,.1f')  , '% | ' , ('#' * int(Food)))
print("Travel | $" , format(Travel, '11,.2f') , " | " , format(Travel, '5,.1f')  , '% | ' , ('#' * int(Travel)))
print(" Extra | $" , format(Tax, '11,.2f') , " | " , format(Tax, '5,.1f')  , '% | ' , ('#' * int(Tax)))
print("Housing | $" , format(extra, '11,.2f') , " | " , format(extra, '5,.1f')  , '% | ' , ('#' * int(extra)))
print("-----------------------------------------------------------------------")
   
