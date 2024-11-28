# String is a iterable
# Strings can be captured in single, double, triple quotes
# You can concat strings using + operator----> 

print("Prince"+" Punshi")

# Repeat strings using * 
print(("Prince"+" ")*3)


# String indexing- In python- indexing starts from 0

name = "Prince"

print(name[0]) #It will print the P as thats sitting on zero index

print(name[-1]) # It will print the last character of the string

# String Slicing: returns multiple elements of the string, via indexing

print(name[0:2]) # it will take character from 0 & 1 index
print(name[0:6:2]) # it will print every second character form the name string
print(name[::-1])
print(name[::1])

# Length function: len() returns the number of elements in an iterable

print(len(name))
numbers = [1,2,4,5]
print(len(numbers))
print(numbers[0])

# String Methods

# Replace method- to replace something from the strins
message = "I hope it snows tonight!"
print(message.replace("snow","rain"))  # its case sensitive, has to be small "snow"
print(message)
# Find method
print(message.find("snow"))

# Upper and lower method---> upper(), lower()

# Strip method---> removes leading and trailing spaces from the string, and lstrip() removes only leading and rstrip() removes only trailing spaces

# Split method- separates a string into list based on the delimeter
message_list = message.split(" ")
print(message_list)

# join method- combined individual list elements into a single string

print(" ".join(message_list))

# This is the example of f string
first_name = "Prince"
last_name = "Punshi"

print(f"My name is {first_name.upper()} and my last name is {last_name}")
