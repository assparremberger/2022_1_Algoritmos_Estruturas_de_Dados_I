from Cliente import Cliente
from FilaCliente import FilaCliente

fila = FilaCliente()

c1 = Cliente("Maria", 25)
c2 = Cliente("Adalto", 36)
c3 = Cliente("Júlia", 20)

fila.adicionar(c1)
fila.adicionar(c2)
fila.adicionar(c3)
fila.remover()
c4 = Cliente("Suzy", 39)
fila.adicionar(c4)
fila.remover()
fila.remover()
fila.remover()