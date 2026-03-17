'''
def generar_ficha(nombre, precio, stock=0, categoria="General", descuento=0):
    precio_final = precio - (precio * descuento / 100)
    estado       = "✅ OK" if stock > 10 else "⚠️ Stock bajo" if stock > 0 else "❌ Sin stock"
    
    print(f"\n{'='*40}")
    print(f"  {nombre.upper()}")
    print(f"{'='*40}")
    print(f"  Categoría    : {categoria}")
    print(f"  Precio       : ${precio:,.2f}")
    if descuento > 0:
        print(f"  Descuento    : {descuento}%")
        print(f"  Precio final : ${precio_final:,.2f}")
    print(f"  Stock        : {stock} unidades")
    print(f"  Estado       : {estado}")
    print(f"{'='*40}")

# Llamadas con distintos niveles de detalle
generar_ficha("Silla", 1350.50)
generar_ficha("Mesa", 2800.00, stock=10, categoria="Mobiliario")
generar_ficha("Lámpara", 450.00, stock=50, categoria="Iluminación", descuento=15)
'''
'''|

Nota el `if descuento > 0` — la línea de descuento solo aparece si hay descuento. La ficha se adapta sola según los datos.

---

### Bloque 3 — 30 min | Proyecto del día

Crea una función `resumen_venta()` que genere esto:
```
========================================
   RESUMEN DE VENTA
========================================
Cliente  : Juan Pérez
Vendedor : Sin asignar
----------------------------------------
Producto       Cant.   Precio    Subtotal
----------------------------------------
Silla            2   $1,350.50  $2,701.00
Mesa             1   $2,800.00  $2,800.00
Lámpara          3     $450.00  $1,350.00
----------------------------------------
Subtotal  :  $6,851.00
Descuento :      $0.00
Total     :  $6,851.00
========================================

'''



items = [
    {"nombre": "Silla",   "precio": 1350.50, "cantidad": 2},
    {"nombre": "Mesa",    "precio": 2800.00, "cantidad": 1},
    {"nombre": "Lámpara", "precio":  450.00, "cantidad": 3},
]

def resumen_venta(cliente, items, vendedor="Sin asignar", descuento=0):
    print(f"Cliente  : {cliente}")
    print(f"Vendedor : {vendedor}")
    print("----------------------------------------")
    for p in items:
        subtotal_p = p["precio"] * p["cantidad"]
        print(f"{p['nombre']:<14} {p['cantidad']:>3}   ${p['precio']:>8,.2f}   ${subtotal_p:>8,.2f}")
    
    # Agrega esto después del for
    subtotal        = sum(p["precio"] * p["cantidad"] for p in items)
    monto_descuento = subtotal * descuento / 100
    total           = subtotal - monto_descuento

    print("----------------------------------------")
    print(f"Subtotal  : ${subtotal:>10,.2f}")
    print(f"Descuento : ${monto_descuento:>10,.2f}")
    print(f"Total     : ${total:>10,.2f}")
    print("=" * 40)

resumen_venta("Juan Pérez", items, vendedor="María López", descuento=10)
'''
print("========================================")
print("   RESUMEN DE VENTA")
print("========================================")
print("Cliente  : Juan Pérez")
print("Vendedor : Sin asignar")
print("----------------------------------------")
print("Producto       Cant.   Precio    Subtotal")
print("----------------------------------------")
generar_ficha("Silla",1350.50,stock=2,categoria="Mobiliario")
generar_ficha("Mesa",2800.00,categoria="Mobiliario")
generar_ficha("Lampara",450.50,stock=3,categoria="Luminaria")
print("----------------------------------------")

print("========================================")

'''
