a = int(input())

str = ""

if a % 2 == 0:
    str = "even"
else:
    str = "odd"
    
print(f"{a} is {str}")