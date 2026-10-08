
a, b = 1, 2
total = 0

while a <= 4000000:
    if a % 2 == 0:
        total += a

    a, b = b, a + b

print(total)

# works by using 'a' and 'b' as the first two numbers and then adding them, with setting 'a' at the limit of 4000000, do a % 2 = 0 to ensure you know when a is even
