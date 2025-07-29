alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# Función que se encarga de codificar el mensaje
# Recibe el texto original y la cantidad de desplazamiento como parámetros
def encrypt(original_text, shift_amount):
    # Se crea una cadena vacía donde se irá construyendo el mensaje cifrado
    cypher_cesar = ""
    # Recorre cada letra del texto original
    for i in original_text:
        # Encuentra la posición actual de la letra en la lista del alfabeto
        position = alphabet.index(i)
        # Calcula la nueva posición desplazando hacia adelante según el valor de shift_amount
        new_position = position + shift_amount
        # Bucle para que se repita el alfabeto si el usuario desea un número mayor que letras
        new_position %= len(alphabet)
        # Obtiene la nueva letra desde la lista del alfabeto usando la nueva posición
        new_letter = alphabet[new_position]
        # Agrega la letra cifrada a la cadena final
        cypher_cesar += new_letter

    # Imprime el resultado cifrado
    print(f"Here is the encoded result: {cypher_cesar}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
encrypt(text, shift)

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

