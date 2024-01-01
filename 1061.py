from datetime import datetime

# Leer la entrada
inicio_dia = input().split()
inicio_hora = input().split(" : ")
fin_dia = input().split()
fin_hora = input().split(" : ")

# Crear objetos de fecha y hora para el inicio y el final del evento
inicio_fecha = datetime(year=2023, month=4, day=int(inicio_dia[1]), hour=int(inicio_hora[0]), minute=int(inicio_hora[1]), second=int(inicio_hora[2]))
fin_fecha = datetime(year=2023, month=4, day=int(fin_dia[1]), hour=int(fin_hora[0]), minute=int(fin_hora[1]), second=int(fin_hora[2]))

# Calcular la duración del evento
duracion = fin_fecha - inicio_fecha

# Imprimir la duración en días, horas, minutos y segundos
print(f"{duracion.days} dia(s)")
print(f"{duracion.seconds // 3600} hora(s)")
print(f"{(duracion.seconds % 3600) // 60} minuto(s)")
print(f"{duracion.seconds % 60} segundo(s)")
