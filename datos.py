import random 
import json

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

for nombre in productos :
    venta_aleatoria = random.randint(2000 , 10000)
    productos = {
        "nombre":nombre,
        "venta" : venta_aleatoria
    }
    productos.append (productos)

with open ('productos.json' , 'w') as archivo:
    json.dump(productos, archivo , indent=4)


