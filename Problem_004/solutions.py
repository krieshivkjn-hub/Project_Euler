
largest = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j

        if str(product) == str(product)[::-1]:
            if product > largest:
                largest = product

print(largest)

#loop through all 3 digit numbers, multiply each pair and then convert the product to a stringand check whether the string equals its reverse using [::-1], keep track of largest palindrome found
