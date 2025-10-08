import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

#funcion1. fecha valida si puede aparecer en el calendario y no es domingo
#.
#.
#.
def funcion1(dia: int, mes:int, anyo:int) -> bool:
    fecha: datetime.date = datetime.date(day=dia, month=mes, year=anyo)
    
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





if __name__ == '__main__':
    pass