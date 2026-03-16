producto = {"nombre": "Silla", "precio": 1350.50, "stock": 25}

# if / elif / else
if producto["stock"] == 0:
    print(f"{producto['nombre']}: SIN STOCK")
elif producto["stock"] <= 10:
    print(f"{producto['nombre']}: STOCK BAJO ({producto['stock']} unidades)")
else:
    print(f"{producto['nombre']}: Stock OK ({producto['stock']} unidades)")


productos = [
    {"nombre": "Silla",    "precio": 1350.50, "stock": 25},
    {"nombre": "Mesa",     "precio": 2800.00, "stock":  0},
    {"nombre": "Lámpara",  "precio":  450.00, "stock": 50},
    {"nombre": "Archivero","precio": 3500.00, "stock":  8},
]

for p in productos:
    # Clasificación por precio
    if p["precio"] >= 3000:
        categoria = "Premium"
    elif p["precio"] >= 1000:
        categoria = "Estándar"
    else:
        categoria = "Económico"

    # Estado de stock con and
    if p["stock"] == 0:
        estado = "❌ Sin stock"
    elif p["stock"] <= 10 and p["precio"] >= 1000:
        estado = "⚠️  Stock bajo — reabastecer pronto"
    else:
        estado = "✅ OK"

    print(f"{p['nombre']:<12} {categoria:<10} {estado}")
'''

Ejecuta y observa cómo el `and` combina dos condiciones — precio alto Y stock bajo activa la alerta de reabastecimiento. Esa es lógica de negocio real.

---

### Bloque 3 — 30 min | Proyecto del día

Construye un **reporte de alertas de inventario** con este output:
```
==========================================
       REPORTE DE ALERTAS — INVENTARIO
==========================================
Producto      Precio       Categoría   Estado
------------------------------------------
Silla         $1,350.50    Estándar    ✅ OK
Mesa          $2,800.00    Premium     ❌ Sin stock
Lámpara         $450.00    Económico   ✅ OK
Archivero     $3,500.00    Premium     ⚠️  Stock bajo
==========================================
⚠️  Productos que requieren atención: 2
==========================================

'''
print("==========================================")
print("       REPORTE DE ALERTAS — INVENTARIO")
print("==========================================")
print("Producto      Precio       Categoría   Estado")
print("------------------------------------------")
for p in productos:
    categoria = "Premium" if p["precio"] >= 3000 else "Estándar" if p["precio"] >= 1000 else "Económico"
    estado = "❌ Sin stock" if p["stock"] == 0 else "⚠️  Stock bajo — reabastecer pronto" if p["stock"] <= 10 and p["precio"] >= 1000 else "✅ OK"
    print(f"{p['nombre']:<12} ${p['precio']:>10,.2f}    {categoria:<10} {estado}")
print("==========================================")
print(f"⚠️  Productos que requieren atención: {sum(1 for p in productos if p['stock'] == 0 or (p['stock'] <= 10 and p['precio'] >= 1000))}")
print("==========================================")