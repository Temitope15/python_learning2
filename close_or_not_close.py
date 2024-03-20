num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
   diff = num1 - num2
else:
    diff = num2 - num1

if round(diff == 0.01, 2):
    print("Close")
else:
    print("Not close")
print()