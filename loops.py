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
    


