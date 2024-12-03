# Loops: A loop is a block of code which runs until a given condition is met

exchange_rate = 0.88
usd_list = [5.99, 2.99, 3.99, 4.99]

euro_list = []

for price in usd_list:
    euro_list.append(round(price*exchange_rate,2))
    
print(euro_list)

customer_ratings = ["5 stars", "3 stars", "4 stars", "7 stars", "1 stars"]
numeric_ratings = []
for rating in customer_ratings:
    numeric_ratings.append(int(rating[0]))

print(numeric_ratings)
print(round(sum(numeric_ratings)/len(numeric_ratings),3))

# Looping over indices- you need to specify a range (usually the length of an iterable)
new_list = []
for i in range(len(euro_list)):
    new_list.append(round(euro_list[i]*exchange_rate,2))
    
print(new_list)

# Enumerate - is the best of both worlds. The enumerate function will return both the index and item in an iterable as it loops through. it returns the index and element in a tupe

# for index,element in enumerate(list)

list_1 = [1,2,3,4]
list_2 = ["Prince", "Dhwani", "Raval", "Punshi"]

for index, element in enumerate(list_1):
    print(f"The first element of list 2 is {list_2[index]} and the first element of list 1 is {element}")
    
    
# Second example

inventories = [10,14,10,15,8,7]
prices = [2.99,3.99,4.99,5.99,6.99,7.99]
product_values = []
for index,element in enumerate(inventories):
    product_values.append(round(prices[index]*element))
    
print(product_values)

# While loop
x= 0
while x<10 :
    print(x)
    x += 1
    
# Loop Control: statements help refine loop behavior and handle potential errors- break, continue, pass, try & Except
# Try and Except: statements resolve errors in a loop without stopping its execution
# Try: indicates the first block of code to run (which could resultr in an error)
# except: indicates an optional block of code to run in case of an error in the try block

price_list = [5.99, None, 19.99, 24.99, 0, "74.99"]

for price in price_list:
    try:
        affordable = 50//price
        print(f"This is affordable {affordable}")
    except:
        print("The price is not right")
    
    


    


