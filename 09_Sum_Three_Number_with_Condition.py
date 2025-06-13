a=int(input("Enter First Integer : "))
b=int(input("Enter Second Integer : "))
c=int(input("Enter Third Integer : "))

if a==b or b==c or c==a:
    print("Two or more value are equal...")
    total=0
else:
    total=a+b+c
    print(f"Sum of three integers is {total}")