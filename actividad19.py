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
class GalletaRelleno(Galleta,Relleno):
    def __init__(self,nombre,precio,peso,sabor_relleno):
        Galleta.__init__(self,nombre,precio,peso)
        Relleno.__init__(self,sabor_relleno)
    def mostrar_info(self):
        return super().mostrar_info()+ f"|{self.describir_relleno()}"
class InventarioGalletas():
    def __init__(self):
        self.galletas=[]
    def registrar_galleta(self,tipo):
        try:
            nombre= input("Ingrese el nombre de la galleta: ")
            precio= float(input("Ingrese el precio: "))
            peso = int(input("Ingrese el peso: "))
            if tipo == "basica":
                self.galletas.append(Galleta(nombre,precio,peso))
            elif tipo == "chispas":
                cantidad_chispas= int(input("Ingrese la cantidad de chispas"))
                self.galletas.append(GalletaChispas(nombre,precio,peso,cantidad_chispas))
            elif tipo == "rellena":
                sabor_relleno = input("Ingrese el sabor del relleno")
                self.galletas.append(GalletaRelleno(nombre,precio,peso,sabor_relleno))
            print("Galleta registrada")
        except ValueError:
            print("Error: Ingrese un valor valido")
        except Exception as e:
            print("Error al registrar la galleta: ",e)
    def listar_galletas(self):
        if not self.galletas:
            print("No hay galletas registradas")
        else:
            for i in self.galletas:
                print(i.mostrar_info())
    def buscar_por_nombre(self):
        nombre = input("Nombre a buscar: ")
        for g in self.galletas:
            if g.nombre.lower() == nombre.lower():
                print(g.mostrar_info())
                return
        print("Galleta no encontrada")
    def eliminar_por_nombre(self):
        nombre= input("Ingrese el nombre a eliminar: ")
        for g in self.galletas:
            if g.nombre.lower() == nombre.lower():
                self.galletas.remove(nombre)
                print("Galleta eliminada")
            else:
                print("Galleta no encontrada")
