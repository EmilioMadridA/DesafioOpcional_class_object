# Funciones externas
from te import Te

# Input para valorización tanto de sabor como de formato
sabor = int(input("Ingrese el número del sabor deseado (1: Té negro, 2: Té verde, 3: Infusión de hierbas): "))
formato = int(input("Ingrese el formato deseado en gramos (300 o 500): "))

# Obtencion de infomación a partir de la clase, sus atributos y metodos.
nombre_sabor, tiempo, recomendacion = Te.obtener_info_sabor(sabor)
precio = Te.obtener_precio(formato)

# Mostrar en pantalla el detalle del pedido
print("\nDetalle del pedido:")
print(f"Sabor del té: {nombre_sabor}")
print(f"Formato: {formato} gramos")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")