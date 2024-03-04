# Definicion de la clase Te()
class Te():
    # Atributos de la clase
    duracion = 365 #días
    precios = {300: 3000, 500: 5000} # {gr:$$}
    sabores = {
        1: ('Té negro', 3, 'Consumir al desayuno'),
        2: ('Té verde', 5, 'Consumir al medio día'),
        3: ('Infusión de hierbas', 6, 'Consumir al atardecer')
    }

    @staticmethod
    def obtener_info_sabor(sabor):
        """Metodo que retorna el nombre, tiempo de preparación y recomendación de consumo 
            para un sabor específico de té.

        Args:
            sabor (int): Variable que determina el elemento a trabajar, entregado por el usuario

        Returns:
            tuple: Tupla de 3 elementos. Sabor, tiempo y recomendación.
        """
        if sabor in Te.sabores:
            return Te.sabores[sabor]
        else:
            return None

    @staticmethod
    def obtener_precio(formato):
        """Metodo que retorna el precio del formato indicado de té.

        Args:
            formato (int): Entero que indica el formato del producto, en gramos.

        Returns:
            int: Retorna el valor asociado al formato indicado.
        """
        return Te.precios.get(formato, "Formato no disponible")    
