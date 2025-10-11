import datetime
import locale
from math import factorial

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

#funcion1. fecha valida si puede aparecer en el calendario y no es domingo
#.
#.
#.
def funcion1(dia: int, mes:int, anyo:int) -> bool:
    try:
        fecha: datetime.date = datetime.date(day=dia, month=mes, year=anyo)
    except ValueError:
        return False
    
    #.weekday() devuelve 0 para lunes y 6 para domingo
    
    #si es domingo devuelvo false
    
    if fecha.weekday()==6:
        return False
    else:
        return True
      

#fucion2. dos enetros n, k. con n>k. calcula el producto de i=0 a k de ∏ (𝑛 − 𝑖 + 1)
#.
#.
def funcion2(n:int, k:int)-> int:
    assert n>k, "n debe ser mayor que k"
    baseproducto: int = 1
    for i in range (0, k+1):
        baseproducto *= n - i + 1
    return baseproducto


#funcion3. producto serie geometrica an = a1 * r ^(n-1). devolver producto de los k primeros terminos.
#.
#.
def funcion3(a1: int, r: int, k:int) -> int:
    assert k>0, "k no puede ser 0"
    
    baseproducto2: int = 1
    for i in range (1, k+1):
        baseproducto2 *= a1 * r **(i-1)
    return baseproducto2

#funcion4. dos enteros n y k con n>=k calcular el combinatorio n sobre k
#.
#.
def funcion4(n: int, k:int)-> float:
    assert n>=k, " n tieene que ser mayor o igual que k"
    nFactorial: int = math.factorial(n)
    kFactorial: int = math.factorial(k)
    nMenoskFactorial: int = math.factorial(n-k)
    combinatorio: float = nFactorial / (kFactorial * nMenoskFactorial)
    return combinatorio
#combinatorio es n!/(k!*(n-k)!)


#funcion5. enteros n y k con n>=k calcular la suma S(n,k) de la serie de la imagen
#.
#.
def funcion5(n:int, k:int)-> float:
    assert n>=k, 'n tiene que ser >=k)'
    baseSuma: float= 0.0
    for i in range (0, k+1):
        beseSuma += (-1)**i* funcion4(k+1,i+1)*(k-i)**n 
    return 1/math.factorial(k) * baseSuma





if __name__ == '__main__':
    
    pass