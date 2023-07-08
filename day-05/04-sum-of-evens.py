print("Welcome to sum of evens")

# One ay
sum_even = 0
for number in range(1,101):
    if number % 2 == 0:
        sum_even += number

print("The total sum of even numbers is {0}".format(sum_even))

# Second way

sum_even_number = 0

for number in range(2,101,2):
    sum_even_number += number

print("The total sum of even numbers is {0}".format(sum_even_number))