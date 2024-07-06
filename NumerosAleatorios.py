import random

numeroMaximo = 20
intentosMaximos = 5  # Número máximo de intentos permitidos

def generarNumeroAleatorio():
    numeroGenerado = random.randint(0, numeroMaximo)
    return numeroGenerado

def jugar():
    numeroAleatorioGenerado = generarNumeroAleatorio()
    intentosRestantes = intentosMaximos

    while intentosRestantes > 0:
        try:
            numeroUsuario = int(input(f"Intento {intentosMaximos - intentosRestantes + 1} de {intentosMaximos}: Ingresa un número entre 0 y {numeroMaximo}: "))
            if numeroUsuario == numeroAleatorioGenerado:
                print("¡Felicidades! Adivinaste el número.")
                break
            elif numeroUsuario < numeroAleatorioGenerado:
                print("El número que ingresaste es menor al número secreto. Inténtalo de nuevo.")
            else:
                print("El número que ingresaste es mayor al número secreto. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

        intentosRestantes -= 1

    if intentosRestantes == 0:
        print(f"Lo siento, no has adivinado el número en {intentosMaximos} intentos. El número secreto era: {numeroAleatorioGenerado}.")

jugar()
