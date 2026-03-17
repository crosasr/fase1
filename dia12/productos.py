def agregar_producto(productos, nombre, precio, stock):
    productos.append({"nombre": nombre, "precio": precio, "stock": stock})
    return productos

def eliminar_producto(productos, nombre):
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            productos.remove(p)
            return True   # encontrado y eliminado
    return False          # no encontrado

def listar_productos(productos):
    if not productos:
        print("⚠️  No hay productos registrados.")
        return
    print("\n-----------------------------")
    for i, p in enumerate(productos, start=1):
        estado = "✅" if p["stock"] > 0 else "❌"
        print(f"{estado} {i}. {p['nombre']:<12} ${p['precio']:>10,.2f}   stock: {p['stock']}")
    print("-----------------------------")
    print(f"Total: {len(productos)} productos")

def buscar_productos(productos, buscar):
    return [p for p in productos if buscar.lower() in p["nombre"].lower()]