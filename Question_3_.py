def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Sample string
string = 'The quick Brow Fox'

# Call the function to count upper and lower case letters
upper_count, lower_count = count_upper_lower(string)

# Print the results
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)


