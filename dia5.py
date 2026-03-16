productos = [
    {"nombre": "Silla",     "precio": 1350.50, "stock": 25},
    {"nombre": "Mesa",      "precio": 2800.00, "stock":  0},
    {"nombre": "Lámpara",   "precio":  450.00, "stock": 50},
    {"nombre": "Archivero", "precio": 3500.00, "stock":  8},
    {"nombre": "Sillón",    "precio": 5200.00, "stock":  3},
]

# Solo productos disponibles
print("--- Productos disponibles ---")
for p in productos:
    if p["stock"] > 0:
        print(f"  {p['nombre']:<12} stock: {p['stock']}")

# Solo productos con stock crítico (1 a 10 unidades)
print("\n--- Stock crítico ---")
for p in productos:
    if 0 < p["stock"] <= 10:
        print(f"  ⚠️  {p['nombre']} — solo {p['stock']} unidades")

# Solo productos económicos (menos de 1000)
print("\n--- Productos económicos ---")
for p in productos:
    if p["precio"] < 1000:
        print(f"  {p['nombre']:<12} ${p['precio']:,.2f}")

# while — repite mientras la condición sea True
contador = 1
while contador <= 5:
    print(f"Vuelta {contador}")
    contador += 1

print("\n--- break: salir del bucle ---")
# Buscar un producto por nombre
buscar = "Lámpara"
for p in productos:
    if p["nombre"] == buscar:
        print(f"Encontrado: {buscar} — ${p['precio']:,.2f}")
        break   # encontrado, ya no seguimos buscando

print("\n--- continue: saltar un elemento ---")
# Listar todos EXCEPTO los sin stock
for p in productos:
    if p["stock"] == 0:
        continue    # salta este y sigue con el siguiente
    print(f"  {p['nombre']:<12} stock: {p['stock']}")
'''

`break` y `continue` son las dos palabras clave que controlan el flujo dentro de cualquier bucle — las usarás constantemente en la Fase 3 con Flet.

---

### Bloque 3 — 30 min | Proyecto del día

Construye un **buscador de productos por rango de precio:**
```
========================================
     BUSCADOR POR RANGO DE PRECIO
========================================
Precio mínimo : $1,000.00
Precio máximo : $3,000.00
----------------------------------------
Resultados:
  1. Silla        $1,350.50   stock: 25
  2. Mesa         $2,800.00   sin stock
----------------------------------------
Total encontrados: 2
========================================
'''
print("========================================")
print("     BUSCADOR POR RANGO DE PRECIO")
print("========================================")
precio_max = 3000
precio_min = 1000
print(f"Precio mínimo : ${precio_min:,.2f}")
print(f"Precio máximo : ${precio_max:,.2f}")
print("----------------------------------------")
print("Resultados:")
for p in productos:
    if precio_min <= p["precio"] <= precio_max:
        stock_txt = "sin stock" if p["stock"] == 0 else f"stock: {p['stock']}"
        print(f"  {p['nombre']:<12} ${p['precio']:,.2f}   {stock_txt}")
print("----------------------------------------")
print(f"Total encontrados: {len([p for p in productos if precio_min <= p['precio'] <= precio_max])}")
print("========================================")
