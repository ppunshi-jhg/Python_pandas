# Limitation of Lists: can be inefficient when you need to look up specific values, as they can only be accessed vioa indexing. So, if you need to look for the item you have look into the whole list.
# To resolve the above issue we have dictionaries, as dictionarties store key-value pair, where keys are used to look up values.

# Dictionary is represented by {}

item_details = {"skis": [249, 10, "Instock"], "snowboard": [200, 0 , "Outofstock"], "goggles": [100,10,"Instock"]}

print(item_details["goggles"])
print(item_details["goggles"][2])

# To add a new key-value pair in the dictionary is pretty easy: 

item_details["binding"] = [150,5,"instock"]

print(item_details)


new_dictionary = {"dictionary key 1": "Im one", "dictionary key 2": "In two"}

print(new_dictionary)
print(new_dictionary["dictionary key 1"])

new_dictionary["dictionary key 3"]= "Im three"

print(new_dictionary)

# Dictionaries methods: 
# .keys() ----> method is used to get the keys from the dictionary

print(new_dictionary.keys())

# .values()-----> values is used to get the values from the dictionary

print(new_dictionary.values())

#  .items()-----> returns key-value pair from a dictioanry as a list of tuples

print(new_dictionary.items())
for value in new_dictionary:
    print(value)
for key, value in new_dictionary.items():
    print(f"The key is {key} and the value is {value}") 
    
    
customer_sales = {
    "C0001": [224.99,87.36],
    "C0002": [125.56],
    "C0003": [224.35],
    "C0004": [330.55,223.35]
}

print(customer_sales.keys())
print(customer_sales.values())

print(list(customer_sales.keys()))
print(list(customer_sales.values()))

for v in customer_sales.values():
    print(sum(v))
    
new_dict = {}
    
for key, value in customer_sales.items():
    new_dict[key]= sum(value)
    
print(new_dict)

# .get()-----> doesnt return the error even if the key is not present

print(customer_sales.get("C00010"))

# Zip function: combines two iterables, like lists, into a single iterator of tuples

item_list = ["skis","snowboard"]
price_list = [10,20]

print(zip(item_list,price_list))  #zip returns the zip object, you can perform list fuinction to convert into list

print(list(zip(item_list,price_list)))