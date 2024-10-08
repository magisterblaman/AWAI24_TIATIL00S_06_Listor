unique_numbers = []

run = True

while run:
    answer = input("Vänligen mata in ett heltal hejhej: ")
    converted = int(answer)
    if converted in unique_numbers:
        while unique_numbers[0] != converted:
            del unique_numbers[0]
        for i in range(len(unique_numbers)):
            print(unique_numbers[i])
    else:
        unique_numbers.append(converted)

    answer2 = input("Vill du köra igen? ")
    if answer2 == "nej":
        run = False