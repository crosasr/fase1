import csv

productos = [
    {"nombre": "Silla",     "precio": 1350.50, "stock": 25},
    {"nombre": "Mesa",      "precio": 2800.00, "stock": 10},
    {"nombre": "Lámpara",   "precio":  450.00, "stock": 50},
]

# ESCRIBIR — guardar lista en CSV
with open("productos.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["nombre", "precio", "stock"]
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()          # escribe la fila de encabezados
    writer.writerows(productos)   # escribe todos los productos

print("✅ Archivo guardado.")

# LEER — cargar CSV en lista de diccionarios
productos_cargados = []
with open("productos.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        productos_cargados.append({
            "nombre": row["nombre"],
            "precio": float(row["precio"]),
            "stock" : int(row["stock"])
        })

print(f"✅ {len(productos_cargados)} productos cargados.")
for p in productos_cargados:
    print(f"  {p['nombre']:<12} ${p['precio']:,.2f}   stock: {p['stock']}")

