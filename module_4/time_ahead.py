hour = int(input("Enter hour: "))
choose = int(input("am (1) or pm (2)? "))
ahead = int(input("How many hours ahead? "))
calc = hour + ahead
if choose == 1 and calc > 12:
    print("New hour:", calc % 12, "pm")
elif choose == 1 and calc < 12:
    print("New hour:", calc, "am")
elif choose == 2 and calc > 12:
    print("New hour:", calc % 12, "am")
else:
    print("New hour:", calc, "pm")

