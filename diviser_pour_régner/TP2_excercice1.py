nb = int(input("Enter a number: "))
max = int(input("entre max interval"))
min = int(input("Enter min interval: "))

while min>max:
    min , max= max, min

ok = nb>min and nb<max

if ok:
    print("The number is good")
else:
    print("The number is bad")