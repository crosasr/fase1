def valor_inventario(productos):
    return sum(p["precio"] * p["stock"] for p in productos)

def total_focos_rojos(productos):
    return len([p for p in productos if 0 < p["stock"] <= 10])

def producto_mas_valioso(productos):
    disponibles = [p for p in productos if p["stock"] > 0]
    if not disponibles:
        return None
    return max(disponibles, key=lambda p: p["precio"] * p["stock"])

def resumen_kpis(productos):
    if not productos:
        return None
    mas_valioso = producto_mas_valioso(productos)
    return {
        "total_productos" : len(productos),
        "valor_inventario": valor_inventario(productos),
        "focos_rojos"     : total_focos_rojos(productos),
        "mas_valioso"     : mas_valioso["nombre"] if mas_valioso else "Sin productos"
    }