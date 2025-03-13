import math

def calcular_hipotenusa(cateto_oposto:float, cateto_adjacente:float) -> float:
    """ Função para retornar a hipotenusa

    Parameters
    ----------
    cateto_oposto : float
        Cateto oposto em formato float
    cateto_adjacente : float
        Cateto adjacente em formato float

    Returns
    -------
    float
        Hipotenusa dos catetos de entrada em formato float

    Exemplo:
    -------
        .. code-block:: python
            print(calcular_hipotenusa(2, 2))
    """

    hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
    return hipotenusa

print(f"A hipotenusa é : {calcular_hipotenusa(float(input("qual o cateto oposto ?")), float(input("qual o cateto adjacente ?")))}")
