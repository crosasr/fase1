# Lista de productos
productos = ["Silla", "Mesa", "Lámpara", "Escritorio"]

print(productos)          # → ['Silla', 'Mesa', 'Lámpara', 'Escritorio']
print(productos[0])       # → Silla (el índice empieza en 0)
print(productos[-1])      # → Escritorio (el último siempre es -1)
print(len(productos))     # → 4 (cuántos elementos tiene)

# Agregar un producto
productos.append("Archivero")
print(productos)

# Eliminar un producto por nombre
productos.remove("Mesa")
print(productos)

# Ordenar alfabéticamente
productos.sort()
print(productos)

for i, producto in enumerate(productos, start=3):
    print(f"{i}. {producto}")
'''

`enumerate` te da el índice y el valor al mismo tiempo. Lo usarás constantemente para mostrar menús y listados.
'''

'''

### Bloque 3 — 30 min | Proyecto del día

Construye un script con un **catálogo de 5 productos** que muestre esto:
'''

'''
=============================
     CATÁLOGO DE PRODUCTOS
=============================
1. Archivero
2. Escritorio
3. Lámpara
4. Mesa
5. Silla
=============================
Total de productos: 5
=============================
'''

productos = ["Archivero", "Escritorio", "Lámpara", "Mesa", "Silla"]
productos.sort()

print("================================")
print("     CATÁLOGO DE PRODUCTOS")
print("================================")
for i, producto in enumerate(productos, start=1):
    print(f"{i}. {producto}")
print("================================")
print(f"Total de productos: {len(productos)}")
print("================================")

