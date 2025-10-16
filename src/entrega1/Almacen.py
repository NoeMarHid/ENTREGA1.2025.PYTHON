import dataclasses
from dataclasses import dataclass
from builtins import staticmethod


#clase para representar las coordenadas en 2D

@dataclass(frozen= True)
class Coordenadas2D:
    latitud: float
    longitud: float
    
    #necesitamos un constructor que reciba una cadena de texto con el formato "latitud,longitud"
    
    @staticmethod
    def of(latitud: float, longitud: float)-> 'Coordenadas2D':
        return Coordenadas2D(latitud, longitud)
    
    

#clase principal Almacen

@dataclass(frozen=True) 
class Almacen:
    #propiedades
    codigo: int # Identificador único del almacén
    nombre: str # tipo de elementos que vende el almacen
    ciudad: str # ciudad donde se encuentra el almacen
    coordenadas: Coordenadas2D # coordenadas del almacen
    
    #creacion de un almacen
    
    @staticmethod
    
    def of(self, codigo: int, nombre: str, ciudad: str, coordenadas: Coordenadas2D) -> 'Almacen':
        return Almacen.of(codigo, nombre, ciudad, coordenadas)
    
    @staticmethod
    
    def parse(self, texto: str) -> 'Almacen':
        partes: list [str] = tecto.split(",")
        
        # evitar que me den una informacion incompleta
        assert len(partes) == 5, "tienes que dar 5 datos: codigo, nombre, ciudad, latitud, longitud"
        
        codigo: int = int(partes[0])
        nombre: str = partes[1]
        ciudad: str = partes[2]
        latitud: float = float(partes[3])
        longitud: float = float(partes[4])
        coordenadas: Coordenadas2D = Coordenadas2D.of(latitud, longitud)
        
    
    
    