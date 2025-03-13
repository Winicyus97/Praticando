import tkinter as tk
from tkinter import filedialog
import pygame
import os


pygame.mixer.init()


def carregar_musica():
    arquivo = filedialog.askopenfilename(
        title="Selecione uma música",
        filetypes=(("Arquivos MP3", "*.mp3"), ("Todos os arquivos", "*.*"))
    )
    if arquivo:
        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.play()
        nome_musica.set(os.path.basename(arquivo)) 


def pausar_musica():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        botao_pausar.config(text="Retomar")
    else:
        pygame.mixer.music.unpause()
        botao_pausar.config(text="Pausar")


def parar_musica():
    pygame.mixer.music.stop()
    nome_musica.set("Nenhuma música carregada")


janela = tk.Tk()
janela.title("Reprodutor de Música MP3")
janela.geometry("400x150")


nome_musica = tk.StringVar()
nome_musica.set("Nenhuma música carregada")


rotulo_musica = tk.Label(janela, textvariable=nome_musica, font=("Arial", 12))
rotulo_musica.pack(pady=10)


botao_carregar = tk.Button(janela, text="Carregar Música", command=carregar_musica)
botao_carregar.pack(pady=5)


botao_pausar = tk.Button(janela, text="Pausar", command=pausar_musica)
botao_pausar.pack(pady=5)


botao_parar = tk.Button(janela, text="Parar", command=parar_musica)
botao_parar.pack(pady=5)


janela.mainloop()