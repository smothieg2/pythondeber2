# Inicializar contador de números pares
cantidad_pares = 0

# Leer 5 valores enteros
for _ in range(5):
    valor = int(input())
    
    # Verificar si el valor es par
    if valor % 2 == 0:
        cantidad_pares += 1

# Imprimir la cantidad de números pares
print(f"{cantidad_pares} numero(s) par(es)")
