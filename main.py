prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47]

user_prime_str = input("Vilket tal vill du kolla? ")
user_prime = int(user_prime_str)

if user_prime in prime_numbers:
    print(str(user_prime) + " är ett primtal")
else:
    print(str(user_prime) + " är inte ett primtal")