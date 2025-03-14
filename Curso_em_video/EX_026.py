frase = input("Digite uma frase: ")


frase_maiuscula = frase.upper()


quantidade_a = frase_maiuscula.count("A")


primeira_posicao = frase_maiuscula.find("A")


ultima_posicao = frase_maiuscula.rfind("A")


print(f"Quantidade de vezes que a letra 'A' aparece: {quantidade_a}")
print(f"Posição da primeira ocorrência da letra 'A': {primeira_posicao}")
print(f"Posição da última ocorrência da letra 'A': {ultima_posicao}")