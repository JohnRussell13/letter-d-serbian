import re

# Specify the path to your file
file_path = 'Serbian (Latin).dic'

# Read the file and extract words
with open(file_path, 'r') as file:
    words = file.read().split()

# Remove first line (number of words)
words = words[1:]

# Define the regular expression pattern
pattern = re.compile(r'\bd\w*', re.IGNORECASE)

# Filter words using the regular expression
filtered_words = list(filter(pattern.match, words))

# Print or do further processing with the filtered words
print(filtered_words)