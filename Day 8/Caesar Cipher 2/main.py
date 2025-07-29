alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# Función principal que recibe el texto, el desplazamiento y si se desea cifrar o descifrar
def caesar(original_text, shift_amount, encode_or_decode):

    # Función interna para cifrar el texto (encode)
    def encrypt(original_text, shift_amount):
        encrypt_text = ""  # Inicializa una cadena vacía para el texto cifrado
        for letter in original_text:  # Recorre cada letra del texto original
            shifted_position = alphabet.index(letter) + shift_amount  # Calcula la nueva posición desplazada
            shifted_position %= len(alphabet)  # Asegura que la posición no se salga del alfabeto
            encrypt_text += alphabet[shifted_position]  # Añade la letra cifrada al resultado
        print(f"Here is the encoded result: {encrypt_text}")  # Muestra el texto cifrado

    # Función interna para descifrar el texto (decode)
    def decrypt(original_text, shift_amount):
        decrypt_text = ""  # Inicializa una cadena vacía para el texto descifrado
        for letter in original_text:  # Recorre cada letra del texto original
            shifted_position = alphabet.index(letter) - shift_amount  # Calcula la nueva posición desplazada
            shifted_position %= len(alphabet)  # Asegura que la posición no se salga del alfabeto
            decrypt_text += alphabet[shifted_position]  # Añade la letra descifrada al resultado
        print(f"Here is the decrypt result: {decrypt_text}")  # Muestra el texto descifrado

    # Según la opción proporcionada por el usuario, se llama a la función de cifrado o descifrado
    if encode_or_decode == "encode":
        encrypt(original_text, shift_amount)  # Llama a la función de cifrado
    elif encode_or_decode == "decode":
        decrypt(original_text, shift_amount)  # Llama a la función de descifrado
    else:
        print("Invalid option. Please choose 'encode' or 'decode'.")  # Mensaje si la opción no es válida

# Llamada a la función principal con los datos ingresados por el usuario
caesar(text, shift, direction)