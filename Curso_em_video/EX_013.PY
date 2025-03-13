salario = float(input("qual o salario a receber o almento? "))

novo = salario + (salario * 15 / 100)

print("com o reajuste de 15 % , o salario vai para R${:.2f}".format(novo))