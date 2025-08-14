class Galleta: #Clase padre de galleta
    def __init__(self,nombre,precio,peso):
        self.nombre=nombre
        self.precio=precio
        self.peso=peso
    def mostrar_info(self):
        return f"Galleta: {self.nombre}|Precio: {self.precio}|Peso: {self.peso}"
class GalletaChispas(Galleta): #Clase hija de Galleta
    def __init__(self,nombre,precio,peso,cantidad_chispas):
        super().__init__(nombre,precio,peso)
        self.cantidad_chispas=cantidad_chispas
    def mostrar_info(self):
        return super().mostrar_info()+ f"|Chispas: {self.cantidad_chispas}"
class Relleno: #Clase Padre Relleno
    def __init__(self,sabor_relleno):
        self.sabor_relleno=sabor_relleno
    def describir_relleno(self):
        return f"Relleno sabor a {self.sabor_relleno}"
class GalletaRelleno(Galleta,Relleno): #Clase con herencia multiple
    def __init__(self,nombre,precio,peso,sabor_relleno):
        Galleta.__init__(self,nombre,precio,peso)
        Relleno.__init__(self,sabor_relleno)
    def mostrar_info(self):
        return super().mostrar_info()+ f"|{self.describir_relleno()}"
class InventarioGalletas(): #Clase para controlar inventario
    def __init__(self):
        self.galletas=[] #Lista para guardar la información ingresada
    def registrar_galleta(self,tipo): #Metodo para registrar la galleta segun el tipo
        try:
            while True:
                nombre= input("Ingrese el nombre de la galleta: ")
                if not nombre:
                    print("El nombre no puede estar vacio")
                else:
                    break
            for i in self.galletas:
                if i.nombre.lower()== nombre.lower():
                    print("El nombre ya ha sido registrado")
                    return
            while True:
                precio= float(input("Ingrese el precio: "))
                if precio <=0:
                    print("El precio debe ser mayor a cero")
                else:
                    break
            while True:
                peso = int(input("Ingrese el peso en gramos: "))
                if peso <=0:
                    print("El peso debe ser mayor a cero")
                else:
                    break
            if tipo == "basica":
                self.galletas.append(Galleta(nombre,precio,peso))
            elif tipo == "chispas":
                while True:
                    cantidad_chispas= int(input("Ingrese la cantidad de chispas: "))
                    if cantidad_chispas < 0:
                        print("La cantidad de chispas debe ser un numero entero positivo")
                    else:
                        break
                self.galletas.append(GalletaChispas(nombre,precio,peso,cantidad_chispas))
            elif tipo == "rellena":
                while True:
                    sabor_relleno = input("Ingrese el sabor del relleno: ")
                    if not sabor_relleno:
                        print("El sabor no puede quedar vacio")
                    else:
                        break
                self.galletas.append(GalletaRelleno(nombre,precio,peso,sabor_relleno))
            print("Galleta registrada")
        except ValueError:
            print("Error: Ingrese un valor valido")
        except Exception as e:
            print("Error al registrar la galleta: ",e)
    def listar_galletas(self): #Clase para listar las galletas
        if not self.galletas:
            print("No hay galletas registradas")
        else:
            for i in self.galletas:
                print(i.mostrar_info())
    def buscar_por_nombre(self): #Metodo para buscar galleta y mostrar su informacion
        nombre = input("Nombre a buscar: ")
        for g in self.galletas:
            if g.nombre.lower() == nombre.lower():
                print(g.mostrar_info())
                return
        print("Galleta no encontrada")
    def eliminar_por_nombre(self): #Metodo eliminar galleta por su nombre
        nombre= input("Ingrese el nombre a eliminar: ")
        for g in self.galletas:
            if g.nombre.lower() == nombre.lower():
                self.galletas.remove(g)
                print("Galleta eliminada")
                return
        else:
            print("Galleta no encontrada")
inventario= InventarioGalletas() #Instancia para el InventarioGalletas
while True: #Menu llamando a cada metodo
    print("----MENU----")
    print("1. Registrar galleta básica")
    print("2. Registrar galleta con chispas")
    print("3. Registrar galleta con relleno")
    print("4. Listar galletas")
    print("5. Buscar galleta por nombre")
    print("6. Eliminar galleta por nombre")
    print("7. Salir")
    opcion = input("Ingrese una de las opciones: ")
    match opcion:
        case "1":
            inventario.registrar_galleta("basica")
        case "2":
            inventario.registrar_galleta("chispas")
        case "3":
            inventario.registrar_galleta("rellena")
        case "4":
            inventario.listar_galletas()
        case "5":
            inventario.buscar_por_nombre()
        case "6":
            inventario.eliminar_por_nombre()
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion invalida. Ingrese una opcion valida")