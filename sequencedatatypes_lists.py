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