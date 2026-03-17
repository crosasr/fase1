# Sin funciones — código repetido
precio1 = 1350.50
total1  = precio1 * 5
print(f"Total: ${total1:,.2f}")

precio2 = 2800.00
total2  = precio2 * 3
print(f"Total: ${total2:,.2f}")

# Con función — una sola definición, múltiples usos
def calcular_total(precio, cantidad):
    return precio * cantidad

print(f"Total: ${calcular_total(1350.50, 5):,.2f}")
print(f"Total: ${calcular_total(2800.00, 3):,.2f}")


def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento / 100)

def clasificar_producto(precio):
    if precio >= 3000:
        return "Premium"
    elif precio >= 1000:
        return "Estándar"
    else:
        return "Económico"

def estado_stock(stock):
    if stock == 0:
        return "❌ Sin stock"
    elif stock <= 10:
        return "⚠️  Stock bajo"
    else:
        return "✅ OK"


print(aplicar_descuento(1350.50, 10))   # → 10% de descuento
print(clasificar_producto(2800))         # → Estándar
print(estado_stock(0))                   # → ❌ Sin stock
print(estado_stock(5))                   # → ⚠️  Stock bajo
print(estado_stock(25))                  # → ✅ OK

'''

### Bloque 3 — 30 min | Proyecto del día

Usa las funciones del Bloque 2 para generar este reporte limpio:
```
============================================
   REPORTE DE PRECIOS CON DESCUENTOS
============================================
Producto       Precio orig.  Descuento  Precio final  Categoría
--------------------------------------------
Silla          $1,350.50      10%        $1,215.45     Estándar
Mesa           $2,800.00       5%        $2,660.00     Estándar
Lámpara          $450.00      15%          $382.50     Económico
Archivero      $3,500.00       8%        $3,220.00     Premium
Sillón         $5,200.00      20%        $4,160.00     Premium
============================================
Ahorro total del cliente: $812.55
============================================
'''


productos = [
    {"nombre": "Silla",     "precio": 1350.50, "descuento": 10},
    {"nombre": "Mesa",      "precio": 2800.00, "descuento":  5},
    {"nombre": "Lámpara",   "precio":  450.00, "descuento": 15},
    {"nombre": "Archivero", "precio": 3500.00, "descuento":  8},
    {"nombre": "Sillón",    "precio": 5200.00, "descuento": 20},
]
print("============================================")
print("   REPORTE DE PRECIOS CON DESCUENTOS")
print("============================================")
print("Producto       Precio orig.  Descuento  Precio final  Categoría")
print("--------------------------------------------")
for p in productos:
    precio_final = aplicar_descuento(p["precio"], p["descuento"])
    categoria    = clasificar_producto(p["precio"])
    print(f"{p['nombre']:<14} ${p['precio']:>10,.2f}   {p['descuento']:>3}%   ${precio_final:>10,.2f}   {categoria}")
print("--------------------------------------------")
ahorro_total = sum(p["precio"] - aplicar_descuento(p["precio"], p["descuento"]) for p in productos)
print("============================================")
print(f"Ahorro total del cliente: ${ahorro_total:,.2f}")
print("============================================")