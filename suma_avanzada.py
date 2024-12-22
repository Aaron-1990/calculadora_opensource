# suma_avanzada.py
def suma_n_numeros():
    """
    Permite sumar N cantidad de números ingresados por el usuario
    """
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor ingrese un número válido")
    
    return sum(numeros)