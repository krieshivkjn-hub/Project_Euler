
number = 600851475143
factor = 2

while factor * factor <= number:
    if number % factor == 0:
        number //= factor
    else:
        factor += 1

print(number)

#starts with the smallest possible prime factor and checks whether that number is divisble by factor, otherwise increase by 1, continue until factor by factor is larger than number
