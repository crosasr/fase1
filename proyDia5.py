# Lista de productos con precio y stock
productos = [
    {"nombre": "Silla", "precio": 1350, "stock": 25},
    {"nombre": "Mesa", "precio": 2800, "stock": 5},
    {"nombre": "Lámpara", "precio": 450, "stock": 0},
    {"nombre": "Escritorio", "precio": 4500, "stock": 3},
    {"nombre": "Archivero", "precio": 3500, "stock": 15},
]

# Ejercicio 1: Mostrar solo productos con stock > 0
print("=== PRODUCTOS DISPONIBLES ===")
for p in productos:
    if p["stock"] > 0:
        print(f"{p['nombre']} - ${p['precio']} - Stock: {p['stock']}")

# Ejercicio 2: Productos premium (precio >= 3000)
print("\n=== PRODUCTOS PREMIUM ===")
for p in productos:
    if p["precio"] >= 3000:
        print(f"⭐ {p['nombre']} - ${p['precio']}")

# Ejercicio 3: Contador con while
print("\n=== STOCK BAJO (while) ===")
stock_bajo = 0
i = 0
while i < len(productos):
    if productos[i]["stock"] <= 10:
        stock_bajo += 1
    i += 1
print(f"Productos con stock bajo: {stock_bajo}")