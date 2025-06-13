# Write a Python program to count the number of characters (character frequency) in a string
text = input("Enter a string: ")

for char in set(text):
    print(char, ":", text.count(char))