#Write a Python function to insert a string in the middle of a string.

def insert_in_middle(original, insert):
    middle_index = len(original) // 2
    result = original[:middle_index] + insert + original[middle_index:]
    return result
original_string = input("Enter the original string: ")
insert_string = input("Enter the string to insert: ")
result_string = insert_in_middle(original_string, insert_string)
print("Resulting string:", result_string)