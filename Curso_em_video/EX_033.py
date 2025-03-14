numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))


maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3


menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3


print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")