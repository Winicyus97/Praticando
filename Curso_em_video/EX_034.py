salario = float(input("Digite o salário do funcionário: R$ "))


if salario > 1250:
    aumento = salario * 0.10  
    aumento = salario * 0.15  

novo_salario = salario + aumento

print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")