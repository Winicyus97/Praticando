velocidade = float(input("Digite a velocidade do carro (em km/h): "))

limite_velocidade = 80
valor_multa_por_km = 7.00

if velocidade > limite_velocidade:

    excesso = velocidade - limite_velocidade
    
    
    multa = excesso * valor_multa_por_km
    
    
    print(f"Você foi multado por ultrapassar o limite de 80 km/h!")
    print(f"Excesso de velocidade: {excesso:.2f} km/h")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Parabéns! Você está dentro do limite de velocidade.")