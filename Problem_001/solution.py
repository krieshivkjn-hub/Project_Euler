
print(sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0))

# works by using the variable 0 to store the sum, and i % x, where x is an integer to check whether the number is divisible by x
