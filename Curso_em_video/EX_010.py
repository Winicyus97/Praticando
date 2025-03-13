reais=float(input("quanto dinheiro voce tem na carteira : "))

dolar=reais/5.81
franco=reais/6.60
euro=reais/6.31
libra=reais/7.53

print("com R${:.2f} voce pode comprar U${:.2f} em dolar".format(reais,dolar))
print("com R${:.2f} voce pode comprar CHF${:.2f} em franco".format(reais,franco))
print("com R${:.2f} voce pode comprar €${:.2f} em euro".format(reais,euro))
print("com R${:.2f} voce pode comprar £${:.2f} em libra".format(reais,libra))