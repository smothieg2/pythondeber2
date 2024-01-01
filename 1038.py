# Definir constantes para los precios de los productos
PRECIO_PRODUCTO_1 = 4.0
PRECIO_PRODUCTO_2 = 4.5
PRECIO_PRODUCTO_3 = 5.0
PRECIO_PRODUCTO_4 = 2.0
PRECIO_PRODUCTO_5 = 1.5

# Solicitar al usuario ingresar el código del producto y la cantidad
codigo_producto = float(input("Ingrese el código del producto: "))
cantidad_producto = int(input("Ingrese la cantidad del producto: "))

# Calcular el total a pagar según el código del producto y la cantidad
if codigo_producto == 1:
    total_pagar = cantidad_producto * PRECIO_PRODUCTO_1
elif codigo_producto == 2:
    total_pagar = cantidad_producto * PRECIO_PRODUCTO_2
elif codigo_producto == 3:
    total_pagar = cantidad_producto * PRECIO_PRODUCTO_3
elif codigo_producto == 4:
    total_pagar = cantidad_producto * PRECIO_PRODUCTO_4
elif codigo_producto == 5:
    total_pagar = cantidad_producto * PRECIO_PRODUCTO_5
else:
    print("Código de producto no válido")
    total_pagar = 0

# Mostrar el resultado con dos dígitos después del punto decimal
print(f"Total: R$ {total_pagar:.2f}")