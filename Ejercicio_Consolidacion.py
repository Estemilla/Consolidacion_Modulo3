#Inicio 
# Todos los nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking","Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Listas para clasificar
magos = []
cientificos = []
otros = []

# Clasificación de los nombres
for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

# Función para agregar 'El gran' a los magos
def hacer_grandioso(Lista_magos):
    magos_grandiosos = []  # Lista temporal para almacenar magos grandiosos
    for mago in Lista_magos:
        magos_grandiosos.append("El gran" + mago)
    return magos_grandiosos

# Función para imprimir los nombres
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Imprimir la lista completa de nombres antes de ser modificados
print("Lista completa de nombres:")
imprimir_nombres(nombres)

# Modificar la lista de magos
magos_grandiosos = hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos, científicos y otros
print("\nMagos grandiosos:")
imprimir_nombres(magos_grandiosos)

print("\nCientíficos:")
imprimir_nombres(cientificos)

print("\nOtros:")
imprimir_nombres(otros)