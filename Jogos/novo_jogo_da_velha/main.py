import numpy as np
import random
import tkinter as tk
from tkinter import messagebox

# Funções do jogo
def criar_tabuleiro():
    """Cria um tabuleiro 3x3 vazio."""
    return np.zeros((3, 3), dtype=int)

def verificar_vencedor(tabuleiro, jogador):
    """Verifica se um jogador venceu."""
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all(tabuleiro[i, :] == jogador) or all(tabuleiro[:, i] == jogador):
            return True
    if all(tabuleiro.diagonal() == jogador) or all(np.fliplr(tabuleiro).diagonal() == jogador):
        return True
    return False

def tabuleiro_cheio(tabuleiro):
    """Verifica se o tabuleiro está cheio."""
    return not any(0 in linha for linha in tabuleiro)

def movimentos_disponiveis(tabuleiro):
    """Retorna uma lista de movimentos disponíveis."""
    return [(i, j) for i in range(3) for j in range(3) if tabuleiro[i, j] == 0]

# Lógica da IA
def movimento_facil(tabuleiro):
    """IA escolhe um movimento aleatório."""
    return random.choice(movimentos_disponiveis(tabuleiro))

def movimento_medio(tabuleiro, jogador_ia):
    """IA tenta vencer ou bloquear o jogador."""
    jogador_humano = 1 if jogador_ia == 2 else 2

    # Verifica se a IA pode vencer
    for movimento in movimentos_disponiveis(tabuleiro):
        tabuleiro[movimento] = jogador_ia
        if verificar_vencedor(tabuleiro, jogador_ia):
            tabuleiro[movimento] = 0
            return movimento
        tabuleiro[movimento] = 0

    # Verifica se o jogador pode vencer e bloqueia
    for movimento in movimentos_disponiveis(tabuleiro):
        tabuleiro[movimento] = jogador_humano
        if verificar_vencedor(tabuleiro, jogador_humano):
            tabuleiro[movimento] = 0
            return movimento
        tabuleiro[movimento] = 0

    # Escolhe aleatoriamente
    return movimento_facil(tabuleiro)

def minimax(tabuleiro, profundidade, maximizando, jogador_ia):
    """Algoritmo Minimax para o modo difícil."""
    jogador_humano = 1 if jogador_ia == 2 else 2

    if verificar_vencedor(tabuleiro, jogador_ia):
        return 1
    elif verificar_vencedor(tabuleiro, jogador_humano):
        return -1
    elif tabuleiro_cheio(tabuleiro):
        return 0

    if maximizando:
        melhor_valor = -np.inf
        for movimento in movimentos_disponiveis(tabuleiro):
            tabuleiro[movimento] = jogador_ia
            valor = minimax(tabuleiro, profundidade + 1, False, jogador_ia)
            tabuleiro[movimento] = 0
            melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = np.inf
        for movimento in movimentos_disponiveis(tabuleiro):
            tabuleiro[movimento] = jogador_humano
            valor = minimax(tabuleiro, profundidade + 1, True, jogador_ia)
            tabuleiro[movimento] = 0
            melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def movimento_dificil(tabuleiro, jogador_ia):
    """IA usa Minimax para escolher o melhor movimento."""
    melhor_movimento = None
    melhor_valor = -np.inf
    for movimento in movimentos_disponiveis(tabuleiro):
        tabuleiro[movimento] = jogador_ia
        valor = minimax(tabuleiro, 0, False, jogador_ia)
        tabuleiro[movimento] = 0
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_movimento = movimento
    return melhor_movimento

# Interface gráfica
class JogoDaVelha:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo da Velha")
        self.tabuleiro = criar_tabuleiro()
        self.fim_do_jogo = False
        self.dificuldade = "facil"  # Padrão: fácil
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_interface()

    def criar_interface(self):
        """Cria a interface gráfica do jogo."""
        frame = tk.Frame(self.janela)
        frame.pack()

        # Botões do tabuleiro
        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna] = tk.Button(
                    frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda l=linha, c=coluna: self.atualizar_botao(l, c))
                self.botoes[linha][coluna].grid(row=linha, column=coluna)

        # Botão para reiniciar o jogo
        botao_reiniciar = tk.Button(self.janela, text="Reiniciar", font=("Arial", 14), command=self.reiniciar_jogo)
        botao_reiniciar.pack(pady=10)

        # Menu para escolher a dificuldade
        menu_dificuldade = tk.Menu(self.janela)
        self.janela.config(menu=menu_dificuldade)
        opcoes_dificuldade = tk.Menu(menu_dificuldade)
        menu_dificuldade.add_cascade(label="Dificuldade", menu=opcoes_dificuldade)
        opcoes_dificuldade.add_command(label="Fácil", command=lambda: self.escolher_dificuldade("facil"))
        opcoes_dificuldade.add_command(label="Médio", command=lambda: self.escolher_dificuldade("medio"))
        opcoes_dificuldade.add_command(label="Difícil", command=lambda: self.escolher_dificuldade("hard"))

    def atualizar_botao(self, linha, coluna):
        """Atualiza o botão clicado pelo jogador."""
        if self.tabuleiro[linha, coluna] == 0 and not self.fim_do_jogo:
            self.tabuleiro[linha, coluna] = 1
            self.botoes[linha][coluna].config(text="X", state="disabled")
            self.verificar_fim_do_jogo()

            if not self.fim_do_jogo:
                self.jogada_ia()

    def jogada_ia(self):
        """Realiza a jogada da IA."""
        if self.fim_do_jogo:
            return
        if self.dificuldade == "facil":
            movimento = movimento_facil(self.tabuleiro)
        elif self.dificuldade == "medio":
            movimento = movimento_medio(self.tabuleiro, 2)
        elif self.dificuldade == "hard":
            movimento = movimento_dificil(self.tabuleiro, 2)
        self.tabuleiro[movimento] = 2
        self.botoes[movimento[0]][movimento[1]].config(text="O", state="disabled")
        self.verificar_fim_do_jogo()

    def verificar_fim_do_jogo(self):
        """Verifica se o jogo terminou."""
        if verificar_vencedor(self.tabuleiro, 1):
            messagebox.showinfo("Fim do jogo", "Você venceu!")
            self.fim_do_jogo = True
        elif verificar_vencedor(self.tabuleiro, 2):
            messagebox.showinfo("Fim do jogo", "IA venceu!")
            self.fim_do_jogo = True
        elif tabuleiro_cheio(self.tabuleiro):
            messagebox.showinfo("Fim do jogo", "Empate!")
            self.fim_do_jogo = True

    def reiniciar_jogo(self):
        """Reinicia o jogo."""
        self.tabuleiro = criar_tabuleiro()
        self.fim_do_jogo = False
        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna].config(text="", state="normal")

    def escolher_dificuldade(self, nova_dificuldade):
        """Altera a dificuldade do jogo."""
        self.dificuldade = nova_dificuldade
        self.reiniciar_jogo()

# Iniciar o jogo
if __name__ == "__main__":
    janela = tk.Tk()
    jogo = JogoDaVelha(janela)
    janela.mainloop()