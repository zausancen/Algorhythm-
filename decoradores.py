def mayusculas(function):
    def envolve(texto):
        return function(texto).upper()
    return envolve

@mayusculas
def mensaje(nombre = str):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('cesar'))