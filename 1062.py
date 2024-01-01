
# Inicializar variables
cantidad_positivos = 0
suma_positivos = 0

# Leer 6 valores
for _ in range(6):
    valor = float(input())
    
    # Verificar si el valor es positivo
    if valor > 0:
        cantidad_positivos += 1
        suma_positivos += valor

# Imprimir la cantidad de números positivos
print(cantidad_positivos, "número(s) positivo(s)")

# Imprimir el promedio de los valores positivos (con un dígito después del punto decimal)
if cantidad_positivos > 0:
    promedio_positivos = suma_positivos / cantidad_positivos
    print(f"Promedio de los valores positivos: {promedio_positivos:.1f}")
else:
    print("No hay valores positivos")
