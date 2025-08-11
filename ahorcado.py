# se importa la libreria random para elegir palabras aleatorias
import random

# se declara una lista de palabras posibles
PALABRAS = [
    "abracadabra",
    "argentina",
    "uide",
    "juan",
    "perro",
    "python",
    "javascript",
]

# intentos maximos que puede hacer el jugador
INTENTOS_MAX = 6

def elegir_palabra():
    # se selecciona una palabra aleatoria
    return random.choice(PALABRAS)

def mostrar_progreso(palabra, aciertos):
    piezas = []                      # acá vamos guardando letras 
    for letra in palabra:            # recorremos la palabra
        if letra in aciertos:        # si letra esta en las letras acertadas
            piezas.append(letra)     #    sí -> mostramos la letra
        else:
            piezas.append("_")       #    no -> guion bajo
    texto = " ".join(piezas)         # unimos con espacios
    return texto                     # y devolvemos el texto


def pedir_letra(ya_intentadas):
    while True:
        entrada = input("Ingresa una letra: ").strip().lower()  # se pide la letra
        if len(entrada) != 1:                                   # si la letra no tiene una longitud 1
            print("Ingresa SOLO una letra.")                    # se muestra un mensaje para que el usuario ingrese solo una letra
            continue                                            # y se vuelve a pedir la letra
        if entrada in ya_intentadas:                            # si la letra ya se intento
            print("Ya intentaste esa letra. Prueba otra.")      # se muestra un mensaje para que el usuario no intente la misma letra
            continue                                            # y se vuelve a pedir la letra
        return entrada                                          # si todo es correcto se devuelve la letra

def jugar():
    # se selecciona una palabra aleatoria
    palabra = elegir_palabra()
    # separamos las letras de la palabra
    letras_palabra = set(palabra)
    # letras que se van acertando
    aciertos = set()
    # letras que se han intentado
    intentadas = set()
    # intentos restantes
    intentos_restantes = INTENTOS_MAX

    print("¡Bienvenido al Ahorcado!")
    print(f"Tienes {intentos_restantes} intentos.")
    print(mostrar_progreso(palabra, aciertos))

    # si intentos restantes es mayor que cero y los aciertos es distinot que las letras de la palabra se mantiene ejecutando el bucle
    while intentos_restantes > 0 and aciertos != letras_palabra:
        # se pide una letra al usuario
        letra = pedir_letra(intentadas)
        # se añade la letra a las letras que se han intentado
        intentadas.add(letra)

        # si la letra esta dentro de las letras de la palabra se añade a las letras acertadas sino se resta un intento
        if letra in letras_palabra:
            # se añade la letra a las letras acertadas
            aciertos.add(letra)
            print(f"¡Acierto! La letra '{letra}' está en la palabra.")
        else:
            # se resta un intento
            intentos_restantes -= 1
            print(f"Fallo. La letra '{letra}' NO está. Intentos restantes: {intentos_restantes}")

        print("Progreso:", mostrar_progreso(palabra, aciertos))
        print("Letras usadas:", ", ".join(sorted(intentadas)))
        print("-" * 40)

    # si aciertos es igual a las letras de la palabra se termina el juego
    if aciertos == letras_palabra:
        print(f"¡Ganaste! La palabra era: {palabra}")
    else:
        print(f"¡Perdiste! La palabra correcta era: {palabra}")

if __name__ == "__main__":
    # se ejecuta el juego
    jugar()
    
