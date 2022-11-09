print("enter the first number")
a = int(input())
print("enter the second number")
b = int(input())
print("enter the third number")
c = int(input())
if a > b and a > c:
    print(a," is greater")
elif b > c and b > a:
    print(b," is greater")
else:
    print(c,"is greater")