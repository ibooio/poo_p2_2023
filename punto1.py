from __future__ import annotations
from abc import ABC, abstractmethod

class Orden:    
    def __init__(self, nro_orden, monto):
        self.__nro_orden = nro_orden
        self.__monto = monto
        self.__estado = "PENDIENTE"
        self.__metodo_de_pago = None
    
    def get_monto(self):
        return self.__monto
    
    def get_numero(self):
        return self.__nro_orden
        
    def imprimir (self):
        print(f"Nro Orden: {self.__nro_orden}")
        print(f"Monto: {self.__monto}")
        print(f"Estado: {self.__estado}")
        if self.__metodo_de_pago is not None:
            print(f"Método de Pago: {self.__metodo_de_pago}\n")

    def pagar (self, metodo_pago: MetodoPago):
        if self.__estado != "PENDIENTE":
            print("No es posible realizar esta operación.")
        else:
            metodo_pago.pagar(self)
            self.__metodo_de_pago = metodo_pago.get_nombre()
            # Variante a la linea anterior: guardar todo el objeto (strategy) metodoPago self.__metodo_pago = metodo_pago
            # y al momento de imprimir hacer self.__metodo_pago.get_nombre()
            self.__estado = "EN CURSO"

class MetodoPago(ABC):
    @abstractmethod
    def get_nombre (self):
        pass
    
    @abstractmethod
    def pagar (self, orden: Orden):
        pass

class Efectivo(MetodoPago):
    def get_nombre(self):
        return "Efectivo"

    def pagar(self, orden: Orden):
        print(f"Acerquese a la sucursal mas cercana para pagar un total de {orden.get_monto()} por la orden con nro {orden.get_numero()}")

class Transferencia (MetodoPago):
    def get_nombre(self):
        return "Transferencia"
    
    def pagar(self, orden: Orden):
        print(f"Debe transferir un total de {orden.get_monto()} por la orden con nro {orden.get_numero()} al CBU 0000000000000000")

class MercadoPago(MetodoPago):
    def get_nombre(self):
        return "Mercado Pago"
    
    def pagar(self, orden: Orden):
        print(f"A continuación será redireccionado a la web de Mercado Pago para que pueda efectuar el pago por un total de {orden.get_monto()} por la orden con nro {orden.get_numero()}")


orden1 = Orden("1",2000)
orden2 = Orden("2",300)
orden3 = Orden("3",1500)

# Caso de prueba Efectivo
orden1.pagar(Efectivo())
orden1.imprimir()
print("")
# Caso de prueba Transferencia
orden2.pagar(Transferencia())
orden2.imprimir()
print("")
# Caso de prueba MercadoPago
orden3.pagar(MercadoPago())
orden3.imprimir()
print("")
# Caso de prueba orden no pendiente
orden1.pagar(Efectivo())
orden1.imprimir()
