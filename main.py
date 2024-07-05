import json
import statistics
from math import prod
import random 

def cargardatos():
    with open('prodctos.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos


def asignar_vemtas_aleatorias():
    productos = [
    "Café Americano","Té Chai","Croissant",
    "Jugo Naranja","Panini de Pavo y Queso",
    "Pastel de Zanahoria","Espresso Doble",
    "Batido de Frutas","Muffin",
    "Ensalada","Chocolate Caliente",
    "Tarta de Frambuesa","Sándwich de Huevo",
    "Galletas de Avena","Frappé de Caramelo"
    ]
    
    productos = []

    for nombre in productos:
        venta_aleatoria = random.randint( 2000 , 10000)
        productos = {
        "nombre":nombre,
        "venta" : venta_aleatoria
    }
    productos.append (productos)

    with open ('productos.json' , 'w') as archivo:
    json.dump(productos, archivo , indent=4)





def ver_estadisticas():




    print("=== MENÚ ´PRINCIPAL ===")
    print ("1. Asignar montos aleatorios.")
    print ("2. Ver estadísticas.")
    print("3. Salir del programa.")

__MA