# Funciones externas
from te import Te

# Creación de las intancias
te_1 = Te()
te_2 = Te()

# Variables que almacenan el tipo de dato
tipo_te_1 = type(te_1)
tipo_te_2 = type(te_2)

# Impresión en consola
print(f"Tipo de te_1: {tipo_te_1}")
print(f"Tipo de te_2: {tipo_te_2}")

# Verificación de igualdad de tipos
if tipo_te_1 == tipo_te_2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")

