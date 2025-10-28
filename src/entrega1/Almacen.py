from builtins import staticmethod
from dataclasses import dataclass
import dataclasses
import random


#-------------------------------------------
#clase para representar las coordenadas en 2D
#-------------------------------------------
@dataclass(frozen= True)
class Coordenadas2D:
    latitud: float
    longitud: float
    
        
    @staticmethod
    def of(latitud: float, longitud: float)-> 'Coordenadas2D':
        return Coordenadas2D(latitud, longitud)
    
    """
    Creamos un objeto llamado Coordenadas2D y validamos que 
    estas coordenadas esten dentro de
    latitud: -1000 y 1000
    longitud: -1000 y 1000
    """
    if not (-1000.0 <= latitud <= 1000.0):
        raise ValueError(f'latutud {latitud} fuera de rango')
        
    if not (-1000.0 <= longitud <= 1000.0):
        raise ValueError(f'longitud {longitud} fuera de rango')
    

#------------------------
#clase principal Almacen
#------------------------


@dataclass(frozen=True) 
class Almacen:

    #-------
    #atributos
    #-------
    
    codigo: int 
    nombre: str 
    ciudad: str 
    coordenadas: Coordenadas2D
    
    #----------------------------
    #creacion de un almacen con .of
    #----------------------------
    
    @staticmethod 
    
    def of(codigo: int, nombre: str, ciudad: str, coordenadas: Coordenadas2D) -> 'Almacen':
        """
        Crea un objeto Almacen con los datos dados
        y validamos los datos
        """
        if codigo < 0:
            raise ValueError(f'El codigo {codigo} no puede ser negativo')
        
        if len(nombre.strip()) == 0:
            #usamos strip para quitar los espacios en blanco al principio y al final
            raise ValueError('El nombre no puede estar vacio')
        
        if len(ciudad.strip()) == 0:
            raise ValueError('La ciudad no puede estar vacia')
        
        # para Coordenadas2D ya hemos hecho la validacion en su clase
        
        
        return Almacen(codigo, nombre, ciudad, coordenadas)
    
    
    #----------------------------------
    #creacion de un almacen con .parse
    #----------------------------------
    @staticmethod
    
    def parse(texto: str) -> 'Almacen':
        """
        Creamos Almacen a partir de una cadena de texto con .parse
        """
        partes: list [str] = texto.split(",") 
        # evitar que me den una informacion incompleta
        assert len(partes) == 5, "tienes que dar 5 datos: codigo, nombre, ciudad, latitud, longitud"
        
        codigo: int = int(partes[0])
        nombre: str = partes[1]
        ciudad: str = partes[2]
        latitud: float = float(partes[3])
        longitud: float = float(partes[4])
        coordenadas: Coordenadas2D = Coordenadas2D.of(latitud, longitud)
        
        return Almacen.of(codigo, nombre, ciudad, coordenadas)
    
    #-----------------------------------------------
    #creacion de un almecen aleatorio con .random
    #-----------------------------------------------
    @staticmethod
    
    def random() -> 'Almacen':
        """
        Crea un objeto Almacen con datos aleatorios
        """
        
        codigo: int = random.randint (1000, 9999)
        nombre: list[str] = ["Electronica", "Ropa", "Alimentos", "Muebles", "Juguetes", "Deportes", "Libros", "Herramientas"]
        ciudad: list[str] = ["Sevilla", "Malaga", "Cadiz", "Huelva", "Granada", "Almeria", "Cordoba", "Jaen", "Barcelona", "Madrid"]
        latitud: float = round(random.uniform(-99.0, 99.0),5)
        longitud: float = round(random.uniform(-99.0, 99.0), 5)
        
        coordenadas: Coordenadas2D = Coordenadas2D.of(latitud, longitud)
        
        return Almacen.of(codigo, random.choice(nombre), random.choice(ciudad), coordenadas)
    
    #---------------------------------
    #creacion de un alamcen en cadena __str__
    #---------------------------------
    def __str__(self) -> str:
        """
        Devuelve una cadena de texto con los datos del Almacen
        """
        return f'{self.codigo}, {self.nombre}, {self.ciudad}, {self.coordenadas.latitud}, {self.coordenadas.longitud}'
    
    
        
    
    
    