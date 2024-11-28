# Its about True and False
# There are some comparison operators in conditional logic like ==,!=,>=,<= etc
# You cna perform membership tests as well in logic conditionals- like "snow" in message
# Membership Tests: check if a value exists inside an iterable data type(like list, set, strings etc). The keywords "in" and "not in" are used to conduct membership tests

message = "It snows tonight"

print("snow" in message)

# If condition

#  if condition:
#       do this
#  elif:
#       do this
# else:
#      do this

a = 100

if a<100:
    print("a value is less than 100")
elif a==100:
    print("a is 100")
else:
    print("a is greater than 100")