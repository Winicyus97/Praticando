nome_completo = input("Digite o nome completo: ")


partes_nome = nome_completo.split()


if len(partes_nome) > 0:
    primeiro_nome = partes_nome[0] 
    ultimo_nome = partes_nome[-1]   
    print(f"Primeiro nome: {primeiro_nome}")
    print(f"Último nome: {ultimo_nome}")
else:
    print("Nenhum nome foi digitado.")