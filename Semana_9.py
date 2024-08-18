# Semana 9
# Tarea: Sistema de Gestión de Inventarios


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos del producto
        self._id_producto = id_producto  # ID único del producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad en inventario
        self._precio = precio  # Precio del producto

    # Getters y setters para cada atributo
    def get_id_producto(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    # Método para mostrar la información del producto
    def mostrar_info(self):
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"


---------------------------------------------------------------------------------------------