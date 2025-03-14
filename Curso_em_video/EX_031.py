distancia = float(input("Digite a distancia da viagem (em Km): "))


tarifa_ate_200km = 0.50  
tarifa_acima_200km = 0.45  


if distancia <= 200:
    preco_passagem = distancia * tarifa_ate_200km
else:
    preco_passagem = distancia * tarifa_acima_200km


print(f"O preço da passagem para uma viagem de {distancia:.2f} Km é R$ {preco_passagem:.2f}.")