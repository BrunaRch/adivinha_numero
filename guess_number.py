import random
import tkinter as tk
from tkinter import messagebox

# Variáveis globais
guesses = 0  
random_number = 0  

# Função para o chute
def make_guess():
    global guesses
    global random_number

    try:
        user_guess = int(entry_guess.get()) 
    except ValueError:
        messagebox.showwarning("Valor inválido", "Digite um número da próxima vez.")
        return
    
    guesses += 1  # Incremento do número de tentativas

    
    if user_guess == random_number:
        messagebox.showinfo("Você acertou!", f"Você acertou em {guesses} tentativas!")
        root.quit()  # Finaliza o jogo após o acerto
    elif user_guess > random_number:
        messagebox.showinfo("Chute alto", "Você chutou muito alto!")
    else:
        messagebox.showinfo("Chute baixo", "Você chutou muito baixo!")

# Função para iniciar o jogo
def start_game():
    global random_number, guesses
    
    try:
        top_of_range = int(entry_range.get()) 
        if top_of_range <= 0:
            messagebox.showwarning("Valor inválido", "Por favor, digite um número maior que 0.")
            return
    except ValueError:
        messagebox.showwarning("Valor inválido", "Digite um número da próxima vez.")
        return
    
    random_number = random.randint(1, top_of_range) 
    guesses = 0  # Reseta o número de tentativas
    label_instructions.config(text="Agora, faça um chute!")

    start_button.config(state=tk.DISABLED) 
    entry_range.config(state=tk.DISABLED)  

# Estilização da janela
root = tk.Tk() 
root.title("Jogo Advinhe o número")  
root.geometry("600x390") 

# Cor da janela
root.config(bg="#c1a1e2")

# EStilização dos inputs
label_intro = tk.Label(root, text="Bem-vindo(a)! Tente adivinhar o número que estou pensando!", font=("Roboto", 14, "bold"), bg="#c1a1e2")
label_intro.pack(pady=10)

label_instructions = tk.Label(root, text="Digite um número para o limite máximo: ", font=("Roboto", 12), bg="#c1a1e2")
label_instructions.pack()

entry_range = tk.Entry(root, font=("Arial", 12))
entry_range.pack(pady=5)


start_button = tk.Button(root, text="Iniciar jogo", command=start_game, font=("Roboto", 12, "bold"), bg="#4CAF50", fg="white", relief="raised")
start_button.pack(pady=10)

label_guess = tk.Label(root, text="Agora, faça um chute: ", font=("Roboto", 12), bg="#c1a1e2")
label_guess.pack(pady=10)

entry_guess = tk.Entry(root, font=("Roboto", 12))
entry_guess.pack(pady=5)

guess_button = tk.Button(root, text="Fazer Chute", command=make_guess, font=("Roboto", 12, "bold"), bg="#F45733", fg="white", relief="raised")
guess_button.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
