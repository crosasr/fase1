productos = []

def mostrar_menu():
    print("\n=============================")
    print("   GESTIÓN DE PRODUCTOS")
    print("=============================")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Listar productos")
    print("4. Buscar producto")
    print("5. Salir")
    print("=============================")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre    = input("Nombre del producto: ")
        precio    = float(input("Precio: $"))
        stock     = int(input("Stock inicial: "))
        productos.append({"nombre": nombre, "precio": precio, "stock": stock})
        print(f"✅ '{nombre}' agregado correctamente.")
    elif opcion == "2":
        nombre = input("Nombre del producto a eliminar: ")
        encontrado = False
        for p in productos:
            if p["nombre"].lower() == nombre.lower():
                productos.remove(p)
                print(f"✅ '{nombre}' eliminado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print(f"⚠️  '{nombre}' no encontrado.")
    elif opcion == "3":
        if not productos:
            print("⚠️  No hay productos registrados.")
        else:
            print("\n-----------------------------")
            for i, p in enumerate(productos, start=1):
                estado = "✅" if p["stock"] > 0 else "❌"
                print(f"{estado} {i}. {p['nombre']:<12} ${p['precio']:>10,.2f}   stock: {p['stock']}")
            print("-----------------------------")
            print(f"Total: {len(productos)} productos")
    elif opcion == "4":
        buscar = input("Nombre a buscar: ")
        resultados = [p for p in productos if buscar.lower() in p["nombre"].lower()]
        if not resultados:
            print(f"⚠️  No se encontraron productos con '{buscar}'.")
        else:
            for p in resultados:
                print(f"  {p['nombre']:<12} ${p['precio']:,.2f}   stock: {p['stock']}")

    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("⚠️  Opción no válida")