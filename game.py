import random
 # Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", 
"inteligencia"]

vocales = ["a","e","i","o","ó","u"]

 # Elegir una palabra al azar
secret_word = random.choice(words)

 # Número máximo de intentos permitidos
num_fallos = 10

 # Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
eleccion = input("Elige unos de los niveles: Facil | Medio | Dificil: ")
word_displayed = ""
while True:
    if eleccion == "Facil":
        for letter in secret_word:
            if letter in vocales:
                word_displayed+=letter
            else:
                word_displayed+="_" 
        break        
    elif eleccion == "Medio":
        pos = 0
        for letter in secret_word:
            if pos == 0 or pos == (len(secret_word)-1):
                word_displayed+=letter    
            else:
                word_displayed+="_"
            pos+=1    
        break     
    elif eleccion == "Dificil": 
        word_displayed = "_" * len(secret_word)
        break
    else:
        print("Insertar un nivel de dificultad valido")
        eleccion = input("Elige unos de los niveles: Facil | Medio | Dificil: ")
print(f"Palabra: {word_displayed}")
i =0           
while i  <  num_fallos:
 # Pedir al jugador que ingrese una letra    preguntar al profe sobre este if
    letter = input("Ingresa una letra: ").lower()
    if letter =="":
       print("No es valido un espacio en blanco")
       continue

 # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

 # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
 # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        i+=1
        print(f"Te quedan {10-i} intentos")

    # Mostrar la palabra parcialmente adivinada
    letters = []
    if eleccion =="Facil":
        for letter in secret_word:
            if letter in guessed_letters or letter in vocales:
                letters.append(letter)
            else:
                letters.append("_")        
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")
    elif eleccion =="Medio":
        for letter in secret_word:
            if letter in guessed_letters or letter in word_displayed:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")
    else:
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
        print(f"Palabra: {word_displayed}")               

 # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
    elif i==10:
        print(f"¡Oh no! Has agotado tus intentos.")
        print(f"La palabra secreta era: {secret_word}")