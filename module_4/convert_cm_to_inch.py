len = float(input("Enter a length in cm: "))
if len < 0:
    inch = "Invalid!"
    print("Invalid")
else:
    inch = round(len / 2.54, 2)
    print(len, "cm is equal to ", inch, "inches.", sep='')
