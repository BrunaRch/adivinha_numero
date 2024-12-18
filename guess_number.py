import random 

top_of_range = input("Escreva um número: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Por favor, escreva um número maior que 0 da próxima vez.")
        quit()
else:
    print("Por favor, digite um número da próxima vez.")
    quit()


random_number = random.randint(1, top_of_range)
print(random_number)