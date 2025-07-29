# Importamos el modulo art.py
import art

# Imprime el logo desde el archivo art.py
print(art.logo)

# Lista del alfabeto en minúsculas
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Solicita al usuario si desea cifrar (encode) o descifrar (decode)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# Solicita el mensaje del usuario
text = input("Type your message:\n").lower()
# Solicita el número de posiciones para desplazar las letras
shift = int(input("Type the shift number:\n"))


# Función principal que ejecuta el cifrado o descifrado
def caesar(original_text, shift_amount, encode_or_decode):

    # Función para cifrar el mensaje
    def encrypt(original_text, shift_amount):
        encrypt_text = ""  # Cadena donde se guarda el mensaje cifrado
        for i in original_text:  # Recorre cada letra del texto
            if i in alphabet:  # Verifica si la letra está en el alfabeto
                shifted_position = alphabet.index(i) + shift_amount  # Calcula la nueva posición
                shifted_position %= len(alphabet)  # Asegura que no se pase del final del alfabeto
                encrypt_text += alphabet[shifted_position]  # Agrega la letra cifrada
            else:
                encrypt_text += i  # Si no es letra, la deja igual
        print(f"Here is the encoded result: {encrypt_text}")  # Imprime el resultado cifrado

    # Función para descifrar el mensaje
    def decrypt(original_text, shift_amount):
        decrypt_text = ""  # Cadena donde se guarda el mensaje descifrado
        for i in original_text:  # Recorre cada letra del texto
            if i in alphabet:  # Verifica si la letra está en el alfabeto
                shifted_position = alphabet.index(i) - shift_amount  # Calcula la nueva posición hacia atrás
                shifted_position %= len(alphabet)  # Asegura que no se pase del inicio del alfabeto
                decrypt_text += alphabet[shifted_position]  # Agrega la letra descifrada
            else:
                decrypt_text += i  # Si no es letra, la deja igual
        print(f"Here is the decrypt result: {decrypt_text}")  # Imprime el resultado descifrado

    # Llama a la función correcta según la elección del usuario
    if encode_or_decode == "encode":
        encrypt(original_text, shift_amount)  # Ejecuta cifrado
    elif encode_or_decode == "decode":
        decrypt(original_text, shift_amount)  # Ejecuta descifrado
    else:
        print("Invalid option. Please choose 'encode' or 'decode'.")  # Si la opción no es válida

# Llama a la función caesar() con los datos ingresados por el usuario
caesar(text, shift, direction)


# Pregunta si el usuario desea volver a intentarlo
respuesta = input("Escribe Yes quieres intentarlo de nuevo. De lo contrario, escribe No:\n").lower()

# Ciclo que repite el programa mientras la respuesta sea 'yes'
while respuesta == "yes":

    # Pide nueva elección (encode o decode)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Pide nuevo mensaje
    text = input("Type your message:\n").lower()

    # Pide nuevo número de desplazamiento
    shift = int(input("Type the shift number:\n"))

    # Llama nuevamente a la función caesar con los nuevos datos
    caesar(text, shift, direction)

    # Vuelve a preguntar si desea repetir
    respuesta = input("Escribe Yes quieres intentarlo de nuevo. De lo contrario, escribe no").lower()
