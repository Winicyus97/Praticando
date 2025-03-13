def converter_medidas(metros):
    quilometros = metros / 1000
    hectometros = metros / 100
    decametros = metros / 10
    decimetros = metros * 10
    centimetros = metros * 100
    milimetros = metros * 1000
    
    return quilometros, hectometros, decametros, decimetros, centimetros, milimetros

metros = float(input("Digite a medida em metros: "))

km, hm, dam, dm, cm, mm = converter_medidas(metros)

print(f"{metros} metros é equivalente a:")
print(f"{km} quilômetros (km)")
print(f"{hm} hectômetros (hm)")
print(f"{dam} decâmetros (dam)")
print(f"{dm} decímetros (dm)")
print(f"{cm} centímetros (cm)")
print(f"{mm} milímetros (mm)")