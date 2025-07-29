
name = "oscar"
print(name.title())  # Para convertir las strings en MAYÚSCULAS e imprime sin print


def format_name(f_name, l_name):
    formated_fname = f_name.title() # Para convertir solo la primer string en MAYÚSCULA se guarda en una variable
    formated_lname = l_name.title()
    # Se usa para devolver y asignar un nuevo valor a la función
    return f"{formated_fname} {formated_lname}"

new = format_name("SanTiAgo","cAsas") # Es decir: RETURN asigna su valor en la entrada de la función
                                              # RESULTADO: return f"{formated_fname}{formated_lname}"
                                              # Y este resultado podemos guardarlo en una variable (new)

print(new)