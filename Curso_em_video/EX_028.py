import random

numero_escolhido = random.randint(0, 5)

tentativa = int(input("Tente adivinhar o número que o computador escolheu (entre 0 e 5): "))


if tentativa == numero_escolhido:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou! O número escolhido pelo computador foi {numero_escolhido}.")