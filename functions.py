# A function is a piece of code that can be reused.

item_ratings = [
    ["5 star", "3 star", "1 star"],
    ["4 star", "3 star", "2 star"],
    ["1 star"]
]

for item in item_ratings:
    for rating in item:
        print(int(rating[0]))
        
# Argumentsa of function can be passed in different formats
# Positional arguments: are those which are passed in the order they were defined in the function.

def concatenator(string1,string2):
    return string1+" "+string2

print(concatenator("Hello", "World"))   #Hello will be passed to string1, world will be passed to string2

# Keyword Arguments: can be passed in any order by using the argument's name

print(concatenator(string2 = "World!", string1 = "Hello"))