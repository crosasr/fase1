from validaciones import pedir_entero, pedir_flotante, pedir_opcion_menu
from productos import agregar_producto, eliminar_producto, listar_productos, buscar_productos
from menu import mostrar_menu
from kpis import resumen_kpis
from datos import guardar_csv, cargar_csv

productos = []

productos = cargar_csv()
print(f"📂 {len(productos)} productos cargados.")

while True:
    mostrar_menu()
    opcion = pedir_opcion_menu(6)  # ahora son 6 opciones

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = pedir_flotante("Precio: $")
        stock  = pedir_entero("Stock inicial: ")
        agregar_producto(productos, nombre, precio, stock)
        print(f"✅ '{nombre}' agregado correctamente.")

    elif opcion == "2":
        nombre = input("Nombre a eliminar: ")
        if eliminar_producto(productos, nombre):
            print(f"✅ '{nombre}' eliminado correctamente.")
        else:
            print(f"⚠️  '{nombre}' no encontrado.")

    elif opcion == "3":
        listar_productos(productos)

    elif opcion == "4":
        buscar = input("Nombre a buscar: ")
        resultados = buscar_productos(productos, buscar)
        if not resultados:
            print(f"⚠️  No se encontraron productos con '{buscar}'.")
        else:
            for p in resultados:
                print(f"  {p['nombre']:<12} ${p['precio']:,.2f}   stock: {p['stock']}")

    elif opcion == "5":
        kpis = resumen_kpis(productos)
        if not kpis:
            print("⚠️  No hay productos registrados.")
        else:
            print("\n========================================")
            print("         KPIs DE INVENTARIO")
            print("========================================")
            print(f"Total productos  : {kpis['total_productos']}")
            print(f"Valor inventario : ${kpis['valor_inventario']:,.2f}")
            print(f"Focos rojos      : {kpis['focos_rojos']}")
            print(f"Más valioso      : {kpis['mas_valioso']}")
            print("========================================")

    elif opcion == "6":
        guardar_csv(productos)
        print("💾 Productos guardados.")
        print("¡Hasta luego!")
        break