import re

message = "Lol, this is my message, 1234, wow, this is amazing"

letters = r'[a-zA-Z]'
numbers = r'[0-9]'
special = r'[^a-zA-Z0-9]'

print("Letters:", len(re.findall(letters, message)))
print("Numbers:", len(re.findall(numbers, message)))
print("Special:", len(re.findall(special, message)))
