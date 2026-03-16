nombre_producto = "Silla de oficina"
stock = 25
precio = 1350.00
disponible = True

print(nombre_producto)
print(stock)
print(f"{precio:,.2f}")
print(disponible)

nombre_producto = "Silla de oficina"
stock = 25
precio = 1350.50
disponible = True

print(f"Producto: {nombre_producto}")
print(f"Precio: ${precio}")
print(f"Stock disponible: {stock} unidades")
print(f"¿Disponible?: {disponible}")

precio = 1350.5678

# Sin formato — feo para mostrarle al cliente
print(f"Precio: ${precio}")

# Con formato — 2 decimales siempre
print(f"Precio: ${precio:.2f}")

# Con separador de miles
print(f"Precio: ${precio:,.2f}")

'''

Ejecuta y observa la diferencia visual. El `:,.2f` lo usarás en cada app que hagas para PyMEs.

---

### Bloque 3 — 30 min | Proyecto del día

Crea una ficha completa con al menos **5 variables** y que la salida se vea así:
'''

'''
=============================
     FICHA DE PRODUCTO
=============================
Nombre     : Silla de oficina
Categoría  : Mobiliario
Precio     : $1,350.50
Stock      : 25 unidades
Disponible : Sí
=============================
'''
Nombre     = "Silla de oficina"
Categoría  = "Mobiliario"
Precio     = 1350.50
Stock      = 25
Disponible = True
estado = "Sí" if Disponible else "No"
print("=============================")
print("     FICHA DE PRODUCTO")
print("=============================")
print(f"Nombre     : {Nombre}")
print(f"Categoría  : {Categoría}")
print(f"Precio     : ${Precio:,.2f}")
print(f"Stock      : {Stock} unidades")
print(f"Disponible : {estado}")
print("=============================")
