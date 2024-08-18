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


class Inventario:
    def __init__(self):
        # Lista para almacenar los productos
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar que el ID del producto sea único antes de añadirlo
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        # Eliminar producto por ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        # Actualizar cantidad o precio de un producto por ID
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Buscar productos por nombre (puede haber nombres similares)
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p.mostrar_info())
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Mostrar todos los productos en el inventario
        if self.productos:
            for p in self.productos:
                print(p.mostrar_info())
        else:
            print("El inventario está vacío.")
