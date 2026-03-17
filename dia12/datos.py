import csv
import os

def guardar_csv(productos, archivo="productos.csv"):
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        campos = ["nombre", "precio", "stock"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(productos)

def cargar_csv(archivo="productos.csv"):
    if not os.path.exists(archivo):
        return []    # si no existe, lista vacía
    productos = []
    with open(archivo, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            productos.append({
                "nombre": row["nombre"],
                "precio": float(row["precio"]),
                "stock" : int(row["stock"])
            })
    return productos