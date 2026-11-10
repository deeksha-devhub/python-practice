a = int(input("Enter a: "))
b = int(input("Enter b: "))

#without temp
a,b = b,a
print("a = ",a)
print("b = ",b)

#with temp 
temp = a
a = b
b = temp
print("a = ",a)
print("b = ",b)