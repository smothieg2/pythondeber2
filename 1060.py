# Inicializar el contador de números positivos
cantidad_positivos = 0

# Leer 6 números
for _ in range(6):
    numero = float(input())
    
    # Verificar si el número es positivo (ignorar valores nulos)
    if numero > 0:
        cantidad_positivos += 1

# Imprimir la cantidad total de números positivos
print(f"Cantidad total de números positivos: {cantidad_positivos}")
