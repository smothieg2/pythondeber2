# Leer un número entero entre 1 y 12
numero_mes = int(input())

# Verificar y imprimir el nombre del mes correspondiente
if 1 <= numero_mes <= 12:
    meses = [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    nombre_mes = meses[numero_mes - 1]
    print(nombre_mes)
else:
    print("Número de mes inválido")
