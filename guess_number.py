import random 

print("Bem-vindos ao jogo!")
print("Tente advinhar o número que estou pensando!")

print("Quero que você me dê um número como o máximo que posso pensar, 0 acima!")

print("Se você escolher 100, eu estarei pensando em um número entre 1 e 100.")

top_of_range = input("Escreva um número: ")

if top_of_range.lstrip('-').isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Por favor, escreva um número maior que 0 da próxima vez.")
        quit()
else:
    print("Por favor, digite um número da próxima vez.")
    quit()

# Gera o número aleatório entre 1 e o número informado
random_number = random.randint(1, top_of_range)

guesses = 0

# Loop de adivinhação
while True:
    guesses += 1
    user_guess = input("Faça um chute: ")

    # Verifica se o valor informado é um número inteiro
    if user_guess.lstrip('-').isdigit():
        user_guess = int(user_guess)
    else:
        print("Por favor, digite um número da próxima vez.")
        continue

    # Checa se o chute do usuário é igual ao número gerado
    if user_guess == random_number:
        print('Você acertou!')
        print("Você acertou em", guesses, "tentativas.")
        quit()  # Sai do programa após o acerto
    elif user_guess > random_number:
        print("Você chutou muito alto!")
    else:
        print("Você chutou muito baixo!")
