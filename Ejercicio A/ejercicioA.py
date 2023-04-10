"""a. El día siguiente
Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo."""

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
        self.empleados = []
    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
    def __str__(self):
        return self.nombre

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre

class Edificio:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        ciudad.agregar_edificio(self)
    def __str__(self):
        return self.nombre
class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)
    def __str__(self):
        return self.nombre
    def destruir(self):
        self.edificios = []

class NewYork(Ciudad):
    def __init__(self):
        super().__init__("New York")

class LosAngeles(Ciudad):
    def __init__(self):
        super().__init__("Los Angeles")

class YooHoo(Empresa):
    def __init__(self):
        super().__init__("YooHoo")
        self.martin = Empleado("Martin")
        self.salim = Empleado("Salim")
        self.xing = Empleado("Xing")
        self.edificio_a = Edificio("A", NewYork())
        self.edificio_b = Edificio("B", NewYork())
        self.edificio_c = Edificio("C", LosAngeles())
        self.agregar_empleado(self.martin)
        self.agregar_empleado(self.salim)
        self.agregar_empleado(self.xing)
        self.agregar_edificio(self.edificio_a)
        self.agregar_edificio(self.edificio_b)
        self.agregar_edificio(self.edificio_c)

class NewYorkDestruida(NewYork):
    def __init__(self):
        super().__init__()
        self.edificios = []

yoo_hoo = YooHoo()
print(yoo_hoo)
print(yoo_hoo.martin)
print(yoo_hoo.salim)
print(yoo_hoo.xing)
print(yoo_hoo.edificio_a)
print(yoo_hoo.edificio_b)
print(yoo_hoo.edificio_c)

new_york_destruida = NewYorkDestruida()
yoo_hoo.edificio_a.ciudad = new_york_destruida
yoo_hoo.edificio_b.ciudad = new_york_destruida

