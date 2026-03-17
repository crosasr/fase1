'''
# Variable GLOBAL — vive fuera de funciones, accesible desde cualquier lado
impuesto = 0.16

def calcular_precio_final(precio):
    resultado = precio + (precio * impuesto)  # usa la variable global
    return resultado

print(calcular_precio_final(1350.50))   # → 1566.58
print(impuesto)                         # → 0.16  ✅ accesible fuera
print(resultado)                        # ❌ ERROR — resultado solo existe dentro de la función

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("⚠️  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️  Ingresa solo números enteros.")

def pedir_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("⚠️  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️  Ingresa solo números.")


Prueba escribir letras, números negativos y valores correctos — el programa nunca debe romperse.

---

### Bloque 3 — 30 min | Proyecto del día

Integra `pedir_entero()` y `pedir_flotante()` en el menú del Día 6-7 — el alta de producto ahora no se rompe con inputs inválidos:
```
=============================
   GESTIÓN DE PRODUCTOS
=============================
1. Agregar producto
...
Elige una opción: 1
Nombre del producto: Silla
Precio: $abc
⚠️  Ingresa solo números.
Precio: $-100
⚠️  El valor no puede ser negativo.
Precio: $1350.50
Stock inicial: xyz
⚠️  Ingresa solo números enteros.
Stock inicial: 25
✅ 'Silla' agregado correctamente.
'''

productos = []

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("⚠️  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️  Ingresa solo números enteros.")

def pedir_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("⚠️  El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("⚠️  Ingresa solo números.")

def pedir_opcion_menu():
    while True:
        try:
            opcion = input("Elige una opción: ")
            if opcion in ["1", "2", "3", "4", "5"]:
                return opcion
            else:
                print("⚠️  Opción no válida (1-5)")
        except:
            print("⚠️  Error en la entrada")

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
    opcion = pedir_opcion_menu()

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = pedir_flotante("Precio: $")
        stock = pedir_entero("Stock inicial: ")
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