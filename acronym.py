# Ask for a string 
original_string = input("Convert to Acrynom: ")
# Covert the string to uppercase
original_string = original_string.upper()
# Convert the string into a list 
list_of_words = original_string.split()
# Cycle through the list 
for word in list_of_words:
    # Get the 1st letter of the word and eliminate the newline
    print(word[0], end="")

# Add a newline
print()