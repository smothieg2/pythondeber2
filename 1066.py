
# Inicializar contadores
pares = impares = positivos = negativos = 0

# Leer 5 valores enteros
for _ in range(5):
    valor = int(input())
    
    # Contar valores pares e impares
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    # Contar valores positivos y negativos
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

# Imprimir la información
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
