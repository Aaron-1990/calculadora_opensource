# main.py
def mostrar_menu():
    print("\n=== Calculadora ===")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (N números)")
    print("6. Salir")

def main():
    from sumar import sumar
    from resta import restar
    from multiplicacion import multiplicar
    from dividir import dividir
    from suma_avanzada import suma_n_numeros

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == '6':
            print("¡Hasta luego!")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                resultado = sumar(num1, num2)
                print(f"\nResultado: {num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = restar(num1, num2)
                print(f"\nResultado: {num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
                print(f"\nResultado: {num1} × {num2} = {resultado}")
            elif opcion == '4':
                if num2 == 0:
                    print("\nError: No es posible dividir entre cero")
                else:
                    resultado = dividir(num1, num2)
                    print(f"\nResultado: {num1} ÷ {num2} = {resultado}")

        elif opcion == '5':
            resultado = suma_n_numeros()
            print(f"\nLa suma total es: {resultado}")
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()