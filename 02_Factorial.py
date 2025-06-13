num = int(input("Enter Number: "))

if num < 0:
    print("Factorial Not exist...")
elif num == 0:
    print("Factorial of zero is 1...")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")