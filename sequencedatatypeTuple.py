# Tuples are similar to lists but the only difference is tuples are immutable- so yoou cant change, remove once theyre created
#  and it represents with parenthesis

price_tuple = (1,2,3)

print(price_tuple)
print(price_tuple[0])
print(price_tuple[:3])

print(2 in price_tuple)

print(list(price_tuple))
print(price_tuple)

# Unpacking tuples

a, b, c = price_tuple
print(a,b,c)