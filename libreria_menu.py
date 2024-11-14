from ordenamiento.numeros_burbuja import burbuja
from ordenamiento.numeros_insercion import insercion
from ordenamiento.numeros_seleccion import seleccion
from ordenamiento.numeros_quick import quicksort
from ordenamiento.numeros_heap import heap_sort
from ordenamiento.numeros_radix import radix_sort
from ordenamiento.numeros_shell import shellsort

def solicitar_lista():
    while True:
        try:
            tamaño = int(input("¿Cuántos elementos deseas ordenar? "))
            if tamaño > 0:
                break
            else:
                print("Por favor, ingresa un número entero positivo.")
        except ValueError:
            print("Por favor, introduce un número entero.")

    lista = []
    print("Introduce los elementos para ordenar:")
    for _ in range(tamaño):
        while True:
            try:
                elemento = int(input("Elemento: "))
                lista.append(elemento)
                break
            except ValueError:
                print("Por favor, introduce un número entero.")
    return lista
def menu():
    print("\nSeleccione el método de ordenamiento:")
    print("1 - Burbuja")
    print("2 - Inserción")
    print("3 - Selección")
    print("4 - Quicksort")
    print("5 - Shellsort")
    print("6 - Radix Sort")
    print("7 - Heap Sort")
    print("8 - Salir")
def ordenamientos():
    lista = solicitar_lista()
    print(f"Lista original: {lista}")
    
    while True:
        menu()
        opcion = input("Opción: ")

        if opcion == "1":
            lista_ordenada = burbuja(lista.copy())
            print(f"Lista ordenada con Burbuja: {lista_ordenada}")

        elif opcion == "2":
            lista_ordenada = insercion(lista.copy())
            print(f"Lista ordenada con Inserción: {lista_ordenada}")

        elif opcion == "3":
            lista_ordenada = seleccion(lista.copy())
            print(f"Lista ordenada con Selección: {lista_ordenada}")

        elif opcion == "4":
            lista_ordenada = quicksort(lista.copy())
            print(f"Lista ordenada con Quicksort: {lista_ordenada}")

        elif opcion == "5":
            lista_ordenada = shellsort(lista.copy())
            print(f"Lista ordenada con Shellsort: {lista_ordenada}")

        elif opcion == "6":
            lista_ordenada = radix_sort(lista.copy())
            print(f"Lista ordenada con Radix Sort: {lista_ordenada}")

        elif opcion == "7":
            lista_ordenada = lista.copy()
            heap_sort(lista_ordenada)
            print(f"Lista ordenada con Heap Sort: {lista_ordenada}")

        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

ordenamientos()
