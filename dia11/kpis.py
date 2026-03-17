# kpis.py
def valor_inventario(productos):
    return sum(p["precio"] * p["stock"] for p in productos)

def total_focos_rojos(productos):
    return len([p for p in productos if p["stock"] <= 10 and p["stock"] > 0])

def producto_mas_valioso(productos):
    return max(productos, key=lambda p: p["precio"] * p["stock"])

def resumen_kpis(productos):
    return {
        "total_productos" : len(productos),
        "valor_inventario": valor_inventario(productos),
        "focos_rojos"     : total_focos_rojos(productos),
        "mas_valioso"     : producto_mas_valioso(productos)["nombre"]
    }
'''

En `main.py` importa `kpis` y genera este reporte:
```
========================================
         KPIs DE INVENTARIO
========================================
Total productos  : 5
Valor inventario : $61,762.50
Focos rojos      : 2
Más valioso      : Sillón
========================================
'''