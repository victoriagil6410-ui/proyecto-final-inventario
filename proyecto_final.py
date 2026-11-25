# PROYECTO FINAL DE PROGRAMACIÓN
# Nombre: Victoria Gil Zaragoza
# Código: 223465101
#Fecha: 2 de diciembre de 2026

#Base de datos: diccionario para almacenar productos
inventario = {}
def agregar_producto ():
    print("AGREGAR PRODCUTO")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: $"))
    cantidad = int(input("Cantidad disponible: "))

    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print((f"Producto '{nombre}' agregado con éxito."))

def mostrar_inventario():
    print("Inventario completo")
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return
    print(f"{'Producto':<20} | {'Precio':<10} | {'Cantidad':<8}")
    print("-" * 42)
    for nombre, datos in inventario.items():
        print(f"{nombre:<20} | $ {datos['precio']:<9.2f} | {datos['cantidad']:<8}")

def buscar_producto():
    print("Buscar producto")
    nombre = input("Escribe el nombre del producto: ")
    if nombre in inventario:
        datos = inventario[nombre]
        print(f"Encontrado: {nombre}")
        print(f"Precio: ${datos['precio']: .2f}")
        print(f" Cantidad: {datos['cantidad']}")
    else:
        print(f"'{nombre}' no está registrado.")

def eliminar_producto():
    print("Eliminar producto")
    nombre = input("Nombre del producto a eliminar: ")

    if nombre in inventario:
        del inventario[nombre]
        print(f"'{nombre}' eliminado del inventario.")

    else:
        print(f"No existe un producto llamado '{nombre}'.")

def calcular_total():
    print("Valor total")
    for datos in inventario.values():
        total += datos["precio"] * datos["cantidad"]
    print(f"El valor total del inventario es: ${total: .2f}")

def mostrar_menu():
    print("\n" + "=" * 40)
    print("Sistema de gestión de inventario")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Ver inventario completo")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Calcular valor total")
    print("6. Salir del programa")
    return input("Selecciona una opción (1-6): ")

def main():
    print("¡Bienvenido a tu sistema de inventario!")
    while True:
        opcion = mostrar_menu()

        if opcion =="1":
            agregar_producto()
        elif opcion =="2":
            mostrar_inventario()
        elif opcion =="3":
            buscar_producto()
        elif opcion =="4":
            eliminar_producto()
        elif opcion =="5":
            calcular_total()
        elif opcion =="6":
            print("¡Gracias por usar el sistema! Hasta luego.")

            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__=="__main__":
    main() 



