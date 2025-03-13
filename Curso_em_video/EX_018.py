import math

def calcular_trigonometria (angulo_graus):
    seno = math.sin(anangulo_radiante)
    cosseno = math.cos(anangulo_radiante)
    tangente = math.tan(anangulo_radiante)
    return {
        "seno": seno,
        "cosseno": cosseno,
        "tangente": tangente
    }


angulo_graus = float(input("qual o angulo ? ")) 

anangulo_radiante = math.radians(angulo_graus)

radiante = calcular_trigonometria(angulo_graus) 

print(f"Ângulo: {angulo_graus} graus")
print(f"Seno: {radiante['seno']:.4f}")
print(f"Cosseno: {radiante['cosseno']:.4f}")
print(f"Tangente: {radiante['tangente']:.4f}")