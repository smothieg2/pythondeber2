# Leer el salario del empleado
salario_actual = float(input())

# Definir el porcentaje de aumento
porcentaje_aumento = 0

# Calcular el nuevo salario y el dinero ganado
if salario_actual <= 400:
    porcentaje_aumento = 15
elif salario_actual <= 800:
    porcentaje_aumento = 12
elif salario_actual <= 1200:
    porcentaje_aumento = 10
elif salario_actual <= 2000:
    porcentaje_aumento = 7
else:
    porcentaje_aumento = 4

aumento = salario_actual * (porcentaje_aumento / 100)
nuevo_salario = salario_actual + aumento

# Imprimir los mensajes con los resultados
print(f"Novo salario: {nuevo_salario:.2f}")
print(f"Reajuste ganho: {aumento:.2f}")
print(f"Em percentual: {porcentaje_aumento} %")
