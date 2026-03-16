# Lista → solo nombres
producto = "Silla"

# Diccionario → nombre + datos
producto = {
    "nombre"   : "Silla de oficina",
    "categoria": "Mobiliario",
    "precio"   : 1350.50,
    "stock"    : 25,
    "disponible": True
}

# Acceder a un valor por su clave
print(producto["nombre"])
print(producto["precio"])
print(f"Precio: ${producto['precio']:,.2f}")

productos = [
    {"nombre": "Silla",      "precio": 1350.50, "stock": 25},
    {"nombre": "Mesa",       "precio": 2800.00, "stock": 10},
    {"nombre": "Lámpara",    "precio":  450.00, "stock": 0},
]

for p in productos:
    print(f"{p['nombre']:<12} ${p['precio']:>10,.2f}   stock: {p['stock']}")


'''
=============================
   CATÁLOGO CON DETALLES
=============================
1. Silla
   Precio : $1,350.50
   Stock  : 25 unidades
   Estado : Disponible

2. Mesa
   Precio : $2,800.00
   Stock  : 10 unidades
   Estado : Disponible

3. Lámpara
   Precio :   $450.00
   Stock  : 0 unidades
   Estado : Sin stock
=============================
Total productos : 3
Valor inventario: $17,500.00
=============================
'''
print("================================")
print("   CATÁLOGO CON DETALLES")
print("================================")
for i, p in enumerate(productos, start=1):
    print(f"{i}. {p['nombre']}")
    print(f"   Precio : ${p['precio']:,.2f}")
    print(f"   Stock  : {p['stock']} unidades")
    print(f"   Estado : {'Disponible' if p['stock'] > 0 else 'Sin stock'}")
print("================================")
print(f"Total productos : {len(productos)}")
print(f"Valor inventario: ${sum(p['precio'] * p['stock'] for p in productos):,.2f}")
print("================================")