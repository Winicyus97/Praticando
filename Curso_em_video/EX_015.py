dia=float(input("pro quantos dias ira  alugar o carro ?"))
km=float(input("qual a kilometragem percorrida com o carro ?"))

dia_carro=dia*60
km_percorrido=km*0.15
total=dia_carro+km_percorrido

print("o preço ao utilizar o carro por {} dias é de R${:.2f} ".format(dia,dia_carro))
print("o preço pela qualtidade rodade de {:.0f}km é de R${:.2f} ".format(km,km_percorrido))
print("o total a se pagar pela locação é de R${:.2f}".format(total))