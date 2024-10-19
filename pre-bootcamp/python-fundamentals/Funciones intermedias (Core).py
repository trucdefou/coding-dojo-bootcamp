# 1. Actualizar valores en diccionarios y listas

# Datos iniciales
matriz = [[10, 15, 20], [3, 7, 14]]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 2. Iterar a través de una lista de diccionarios

# 1. Cambiar el valor 3 en matriz por 6
matriz[1][0] = 6
print("Matriz actualizada:", matriz)  # Salida esperada: [[10, 15, 20], [6, 7, 14]]

# 2. Cambiar el nombre del primer cantante a "Enrique Martin Morales"
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes actualizados:", cantantes)

# 3. Cambiar "Cancún" por "Monterrey" en el diccionario ciudades
ciudades["México"][2] = "Monterrey"
print("Ciudades actualizadas:", ciudades)

# 4. Cambiar el valor de la latitud en coordenadas
coordenadas[0]["latitud"] = 9.9355431
print("Coordenadas actualizadas:", coordenadas)


# Definir la función iterarDiccionario
def iterarDiccionario(lista):
    for diccionario in lista:
        salida = []
        for llave, valor in diccionario.items():
            salida.append(f"{llave} - {valor}")
        print(", ".join(salida))  # Imprimir en el formato deseado

# Lista de cantantes
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamar a la función con la lista de cantantes
iterarDiccionario(cantantes)

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])  # Imprime el valor asociado con la clave proporcionada

# Lista de cantantes
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# Llamar a la función con la clave "nombre"
iterarDiccionario2("nombre", cantantes)

print()  # Separador para una salida clara

# Llamar a la función con la clave "pais"
iterarDiccionario2("pais", cantantes)

# funciones_intermedias_1.py

# 1. Función para iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for diccionario in lista:
        salida = []
        for llave, valor in diccionario.items():
            salida.append(f"{llave} - {valor}")
        print(", ".join(salida))

# 2. Función para obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# 3. Función para iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for llave, valores in diccionario.items():
        print(f"{len(valores)} {llave.upper()}")
        for valor in valores:
            print(valor)

# 4. Iterar a través de un diccionario con valores de lista

# Datos de prueba
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# Llamadas de ejemplo a las funciones
print("Iterar a través de lista de diccionarios:")
iterarDiccionario(cantantes)

print("\nObtener valores de una clave específica:")
iterarDiccionario2("nombre", cantantes)

print("\nIterar a través de un diccionario con valores de lista:")
imprimirInformacion(costa_rica)

