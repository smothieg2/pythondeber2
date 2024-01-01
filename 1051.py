# Leer el salario de un habitante de Lisarb
salario = float(input())

# Calcular el impuesto
if salario <= 2000:
    impuesto = 0
else:
    if salario <= 3000:
        impuesto = (salario - 2000) * 0.08
    elif salario <= 4500:
        impuesto = 1000 * 0.08 + (salario - 3000) * 0.18
    else:
        impuesto = 1000 * 0.08 + 1500 * 0.18 + (salario - 4500) * 0.28

# Imprimir el resultado
if impuesto == 0:
    print("Isento")
else:
    print(f"R$ {impuesto:.2f}")
