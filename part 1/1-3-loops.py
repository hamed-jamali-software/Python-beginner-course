number = 0

# define a while loop
while( number < 5):
    print(number)
    number = number + 1

# define a for loop
for number in range(5, 10):
    print(number)

# use a for loop over a collection
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(type(days))
for item in days:
    print(item)

# use the break and continue statements
for number in range(5, 10):
    # if (x == 7): break
    # if (x % 2 == 0): continue
    print(number)

# using the enumerate() function to get index
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for index, item in enumerate(days):
    print(index, item)