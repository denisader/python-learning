nums = [1, 2, 3, 4, 5, 6]

# functions like map and filter return "lazy objects" (iterators)
# they don't actually do the work until you convert them to a list
# or loop over them -> which saves memory
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

print(f"Original: {nums}")
print(f"Squares of evens: {result}")