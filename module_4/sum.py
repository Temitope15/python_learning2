s = 0
for i in range(1,101):
    s = s + i
print("the sum from  1 to 100 is", s)

# print avg of ten nums
# total = 0
# for i in range(10):
#     num = eval(input("Enter a number: "))
#     total = total + num
# print("The average is", total / 10)
x = 5
y = 4
z = 6
w = 7
w,x,y,z = z,y,x,w
print(w,x,y,z)