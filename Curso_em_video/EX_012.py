produto=float(input("qual o valor a receber o desconto R$:"))

novo = produto - (produto*5/100)
print("o desconto do produto com 5% vai para R${:.2f}".format(novo))