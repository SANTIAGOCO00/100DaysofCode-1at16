def format_name(f_name, l_name):
    # DOCSTRINGS: Texto para explicar la funcionalidad de la función
    """Damos un nuevo formato un nuevo formato a los nombres
    Donde la salida será con la primér letra en mayúscula únicamente"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



