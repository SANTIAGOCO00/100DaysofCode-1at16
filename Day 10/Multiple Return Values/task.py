def format_name(f_name, l_name):
    if f_name == "" or l_name == "": # Si no se ingresa datos str...
        return "NO INGRESO UNA OPCIÓN VALIDA" # Devuelve este resultado si se cumple la condición
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}" # Devuelve este resultado si no se cumple la condición

# Imprimimos la función que a su vés pregunta los valores de entrada de la misma...
print(format_name(input("What´s your first name?\n"), input("What´s your second name?\n")))
