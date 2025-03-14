cidade = input("Digite o nome de uma cidade: ")


cidade_formatada = cidade.strip().upper()


if cidade_formatada.startswith("SANTO"):
    print("A cidade começa com 'SANTO'.")
else:
    print("A cidade NÃO começa com 'SANTO'.")