# Lists: are iterable data types capable of storing many individual elements(different data type), and data can be added, rmeoved and changed at any time

random_list = ["Prince",1,"Dhwani",2, True]

# Since lists are iterable, so you can perform membership test in list

if "Princ" in random_list:
    print(f"Prince is in the list")
else:
    print("name is not in the list")
    
# You can perform slicing on lists

print(random_list[0:3:1])

# Very Important: lists elements can be unpackedinto indivoidual variables

a, b, c, d, e = random_list

print(a,b,c,d,e)

# lists elements can be changed, but not added, by using indexing

random_list[2] = "Dhwani Raval"
print(random_list)

# You can use append and insert to add a new element into the list
# .append ---> to add to the end
#  .insert ---> to insert at the specified index

random_list.append("Dushy")
random_list.insert(2, "New baby")
print(random_list)

# Removing list elements: There are two ways to remove list elements
# del keyword: deletes the selected element from the list
# remove: deletes the first occurence of the specified value from the list

del random_list[1:3]  #it will delete the index number 1 and 2 element
random_list.remove("Dushy")

print(random_list)

# You can concatenate two lists together by having the add sign in it

random_list_2 = [1,2,3]
new_list = random_list + random_list_2
print(new_list)

# List functions
# len() len(random_list)
# sum(list_name)
# min(list_name)
# max(list_name)
# sort() ----> The sort() method sorts the list permanently(in place)
# sorted()---> The sorted() function returns a sorted list, but doesnt change the original list
# .index()
# count() and reverse()

customer_ids = ["C0001", "C0002", "C0003", "C0004", "C0005"]
print(f"The customer list count is {customer_ids.count("C0002")}")
print(len(customer_ids))
print(customer_ids.index("C0003"))

# Nesting and copying lists:

nested_list = [["a","b","c"],[1,2,3],["d","e","f"]]

print(nested_list[0])
print(nested_list[0][1])

# You can copy via three ways
# 1. assignment to the other variable- in this case any change to one will affect the other copy

nested_list_2 = nested_list

nested_list[0] = ["aa","bb", "cc"]

print(nested_list_2)

# 2. Shallow copy - via copy() method- it will just change the value of the inside of the nested element for both the lists
# 3. Deep Copy -  via deepcopy() method- both the lists will be independent in this case but you will have to use the deepcopy() method from copy library

