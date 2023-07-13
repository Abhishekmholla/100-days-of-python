print("Welcome to prime number checker")


def prime_checker(number):
    
    is_prime = True
    for num in range(2,number):
        if number % num == 0:
            is_prime = False
        
    return is_prime


number = int(input("Check this number: "))
is_prime = prime_checker(number)

if not is_prime:
    print("It's a normal number")
else:
    print("It is a prime number")