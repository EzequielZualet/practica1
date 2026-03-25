import random
import string

categorias = {
    "Conceptos": ["python", "programa", "variable", "funcion", "bucle", "cadena"],
    "Tipos de datos": ["entero", "lista"],
}

print("¡Bienvenido al Ahorcado!")
print()

# Mostrar categorías UNA sola vez
print("Categorías disponibles:")
nombres_categorias = list(categorias.keys())

for i, nombre in enumerate(nombres_categorias, start=1):
    print(f"{i}. {nombre}")

# Elegir categoría (con validación)
opcion = input("Elegí una categoría (número): ")
while not opcion.isdigit() or not (1 <= int(opcion) <= len(nombres_categorias)):
    print("Entrada no válida")
    opcion = input("Elegí una categoría (número): ")

categoria_elegida = nombres_categorias[int(opcion) - 1]
palabras = categorias[categoria_elegida]

palabras_mezcladas = random.sample(palabras, len(palabras))
score = 0

#recorrer palabras sin repetir
for word in palabras_mezcladas:

    guessed = []
    attempts = 6

    print(f"\nAhorcado - Categoría: {categoria_elegida}")
    print()

    while attempts > 0:

        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

         #Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            score += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        # Una sola letra del alfabeto (no número ni otro símbolo); si no, no cuenta el turno
        if len(letter) != 1 or letter in string.digits or letter not in string.ascii_letters:
            print("Entrada no válida")
            continue

        letter = letter.lower()

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        score = 0

print(f"Puntaje final: {score}")