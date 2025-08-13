class Galleta:
    def __init__(self,nombre,precio,peso):
        if not nombre:
            print("El nombre no puede estar vacio")
        if precio <=0:
            print("El precio debe ser mayor a cero")
        if peso <=0:
            print("El peso debe ser mayor a cero")
        self.nombre=nombre
        self.precio=precio
        self.peso=peso
    def mostrar_info(self):
        return f"Galleta: {self.nombre}|Precio: {self.precio}|Peso: {self.peso}"
class GalletaChispas(Galleta):
    def __init__(self,nombre,precio,peso,cantidad_chispas):
        super.__init__(nombre,precio,peso)
        self.cantidad_chispas=cantidad_chispas
        if cantidad_chispas <0:
            print("La cantidad de chispas no puede ser negativa")
    def mostrar_info(self):
        return super().mostrar_info()+ f"|Chispas: {self.cantidad_chispas}"
class Relleno:
    def __init__(self,sabor_relleno):
        self.sabor_relleno=sabor_relleno
        if not sabor_relleno:
            print("El sabor del relleno no puede estar vacio")
    def describir_relleno(self):
        return f"Relleno sabor a {self.sabor_relleno}"
