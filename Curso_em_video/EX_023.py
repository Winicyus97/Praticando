numero = int(input("Digite um número entre 0 e 9999: "))


if 0 <= numero <= 9999:

    numero_str = f"{numero:04d}"
    
    print(f"Milhar: {numero_str[0]}")
    print(f"Centena: {numero_str[1]}")
    print(f"Dezena: {numero_str[2]}")
    print(f"Unidade: {numero_str[3]}")
else:
    print("Número fora do intervalo válido (0 a 9999).")