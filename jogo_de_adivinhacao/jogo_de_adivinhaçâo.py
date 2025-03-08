import random
import tkinter as tk
from tkinter import messagebox

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")
        self.root.geometry("300x200")

        self.numero_secreto = 0
        self.tentativas = 0
        self.tentativas_maximas = 10
        self.pontuacao = 100
        self.dificuldade = "Médio"

        self.label = tk.Label(root, text="Escolha a dificuldade:")
        self.label.pack(pady=10)

        self.dificuldade_var = tk.StringVar(value="Médio")
        self.dificuldade_facil = tk.Radiobutton(root, text="Fácil (1-50)", variable=self.dificuldade_var, value="Fácil")
        self.dificuldade_medio = tk.Radiobutton(root, text="Médio (1-100)", variable=self.dificuldade_var, value="Médio")
        self.dificuldade_dificil = tk.Radiobutton(root, text="Difícil (1-200)", variable=self.dificuldade_var, value="Difícil")

        self.dificuldade_facil.pack()
        self.dificuldade_medio.pack()
        self.dificuldade_dificil.pack()

        self.botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=self.iniciar_jogo)
        self.botao_iniciar.pack(pady=20)

    def iniciar_jogo(self):
        self.dificuldade = self.dificuldade_var.get()
        if self.dificuldade == "Fácil":
            self.numero_secreto = random.randint(1, 50)
        elif self.dificuldade == "Médio":
            self.numero_secreto = random.randint(1, 100)
        elif self.dificuldade == "Difícil":
            self.numero_secreto = random.randint(1, 200)

        self.tentativas = 0
        self.pontuacao = 100
        self.janela_palpite()

    def janela_palpite(self):
        self.janela = tk.Toplevel(self.root)
        self.janela.title("Faça seu palpite")
        self.janela.geometry("300x150")

        self.label_palpite = tk.Label(self.janela, text=f"Tentativa {self.tentativas + 1} de {self.tentativas_maximas}")
        self.label_palpite.pack(pady=10)

        self.entrada_palpite = tk.Entry(self.janela)
        self.entrada_palpite.pack(pady=10)

        self.botao_palpite = tk.Button(self.janela, text="Enviar Palpite", command=self.verificar_palpite)
        self.botao_palpite.pack(pady=10)

    def verificar_palpite(self):
        try:
            palpite = int(self.entrada_palpite.get())
            self.tentativas += 1

            if palpite < self.numero_secreto:
                messagebox.showinfo("Resultado", "Seu palpite foi muito baixo!")
            elif palpite > self.numero_secreto:
                messagebox.showinfo("Resultado", "Seu palpite foi muito alto!")
            else:
                messagebox.showinfo("Parabéns!", f"Você acertou em {self.tentativas} tentativas!\nSua pontuação: {self.pontuacao}")
                self.janela.destroy()
                return

            if self.tentativas >= self.tentativas_maximas:
                messagebox.showinfo("Fim de Jogo", f"Suas tentativas acabaram! O número era {self.numero_secreto}.")
                self.janela.destroy()
                return

            self.pontuacao -= 10
            self.label_palpite.config(text=f"Tentativa {self.tentativas + 1} de {self.tentativas_maximas}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
    