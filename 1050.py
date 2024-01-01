# Leer el número de código de área
ddd = int(input())

# Definir la tabla de códigos de área y destinos
tabla_ddd = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    # Añade más códigos de área y destinos según sea necesario
}

# Verificar si el DDD está en la tabla e imprimir el destino correspondiente
if ddd in tabla_ddd:
    print(tabla_ddd[ddd])
else:
    print("DDD nao cadastrado")
