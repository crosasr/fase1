from validaciones import pedir_entero, pedir_flotante
from productos import aplicar_descuento, clasificar_producto, estado_stock
from kpis import resumen_kpis

productos = [
    {"nombre": "Silla",     "precio": 1350.50, "stock": 25},
    {"nombre": "Mesa",      "precio": 2800.00, "stock":  0},
    {"nombre": "Lámpara",   "precio":  450.00, "stock": 50},
    {"nombre": "Archivero", "precio": 3500.00, "stock":  8},
    {"nombre": "Sillón",    "precio": 5200.00, "stock":  3},
]

kpis = resumen_kpis(productos)

print("========================================")
print("         KPIs DE INVENTARIO")
print("========================================")
print(f"Total productos  : {kpis['total_productos']}")
print(f"Valor inventario : ${kpis['valor_inventario']:,.2f}")
print(f"Focos rojos      : {kpis['focos_rojos']}")
print(f"Más valioso      : {kpis['mas_valioso']}")
print("========================================")

# Prueba que todo importa correctamente
precio = pedir_flotante("Precio del producto: $")
stock  = pedir_entero("Stock inicial: ")

print(f"Categoría : {clasificar_producto(precio)}")
print(f"Estado    : {estado_stock(stock)}")
print(f"Con 10%   : ${aplicar_descuento(precio, 10):,.2f}")