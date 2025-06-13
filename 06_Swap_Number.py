#Swapping With Temp Variable
a=int(input("Enter A :"))
b=int(input("Enter B :"))

def swap_with_temp(a,b): #a=1 b=2
    temp=a #temp=1
    a=b #a=2
    b=temp #b=1
    return a,b #a=2 b=1

a,b =swap_with_temp(a,b)
print(f"After Swaping With Temp A is {a} and B is {b}")

#Swapping Without 3rd Variable
c=int(input("Enter C :"))
d=int(input("Enter D :"))

def swap_without_temp(c,d): #c=1 d=2
    c = c+d #c=1+2=3
    d = c-d #d=3-2=1
    c = c-d #c=3-1=2
    return c,d #c=2 d=1

c,d =swap_without_temp(a,b)
print(f"After Swaping Without Temp C is {a} and D is {b}")