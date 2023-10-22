import json

# Serbian letters
file_path = 'Letters.txt'
with open(file_path, 'r') as file:
    letters = file.read().split()
letters = ['.', *letters]

# Serbian words
file_path = 'Serbian (Latin).dic'
with open(file_path, 'r') as file:
    words = file.read().split()
words = words[1:]
words = [word.lower() for word in words]
words = ['.'+word+'.' for word in words]

result = {}

# D in middle
for before in letters:
    for after in letters:
        substring = f'{before}d{after}'
        result[substring] = [word for word in words if substring in word]

        if len(result[substring]) > 0:
            result[substring] = result[substring]

result = {key: value for key, value in result.items() if value}
result = {key: [value.strip('.') for value in values] for key, values in result.items()}

file_path = 'output.json'

with open(file_path, 'w') as json_file:
    json.dump(result, json_file, indent=2)