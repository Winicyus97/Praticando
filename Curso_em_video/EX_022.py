nome_completo = input("Digite o nome completo: ")

nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()

quantidade_letras = len(nome_completo.replace(" ", ""))

partes_nome = nome_completo.split()
quantidade_letras_primeiro_nome = len(partes_nome[0])

print(f"Nome em maiúsculas: {nome_maiusculo}")
print(f"Nome em minúsculas: {nome_minusculo}")
print(f"Quantidade de letras ao todo (sem espaços): {quantidade_letras}")
print(f"Quantidade de letras no primeiro nome: {quantidade_letras_primeiro_nome}")

