def fibonacci_series(start,end):
    a=0
    b=1
    while a<=end:
        if a>=start:
            print(a,end=" ")
        a, b = b, a + b

start=int(input("Enter start of range : "))
end=int(input("Enter end of range :" ))

print(f"Fibonacci number between {start} and {end} are : ")
fibonacci_series(start,end)