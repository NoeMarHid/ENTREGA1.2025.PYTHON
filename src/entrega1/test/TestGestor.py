from entrega1.Almacen import Almacen, Coordenadas2D
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


print("*****************")
print("Creacion de un almacen con .of()")
a1 = Almacen.of(9090, "Almacen Zapatos", "Granada", Coordenadas2D.of(45.009,-233.0009))
print(a1)
print("*****************")

print("Creacion de un almacen con parse")
a2 = Almacen.parse("8080;Almacen Ropa;Sevilla;123.009;-456.0001")
print(a2)
print("*****************")

print("Creacion de un almacen aleatorio con .random()")
a3 = Almacen.random()
print(a3)
print("*****************")

print("Creacion con cadena __str__")
a4 = Almacen.parse(str(a3))
print(a4)
print("*****************")


