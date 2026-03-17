def calcular_total(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(precio, descuento=0):
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