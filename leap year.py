print("Enter start year")
start = int(input())
print("Enter last year")
end = int(input())
print("List of leap years:")
for year in range(start, end):
    if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
        print(year)

