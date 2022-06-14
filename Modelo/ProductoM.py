class ProductoM:
    def __init__(self, nombre, descripcion, mercadoObjetivo):
        self.nombre = nombre
        self.descripcion=descripcion
        self.mercadoObjetivo=mercadoObjetivo
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion