import math

def calcular_hipotenusa(cateto_oposto, cateto_adjacente):
    hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
    return hipotenusa

cateto_oposto=float(input("qual o cateto oposto ?"))
cateto_adjacente=float(input("qual o cateto adjacente ?"))

hipotenusa = calcular_hipotenusa(cateto_oposto, cateto_adjacente)
print(f"A hipotenusa é : {hipotenusa}")

