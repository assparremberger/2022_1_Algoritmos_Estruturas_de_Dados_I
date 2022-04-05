# 28/03/2022
from Cidade import Cidade
from Pessoa import Pessoa

c1 = Cidade("Porto Alegre")
#print( "Cidade: ", c1.nome )
#c1.estado = "SC"

p1 = Pessoa("Adalto", "51 98765-4321", "Rua B", 2245.98, c1 )
#p1.salario = 2300.50
p1.cadastrar()

print("---------------------")

p2 = Pessoa("Maria", "51 2233-4455", "Rua C", 3275.95, c1)
#p2.municipio = c1
p2.cadastrar()

c2 = Cidade("Florianópolis")
c2.estado = "SC"

print("---------------------")

p3 = Pessoa("Daniel", "48 22337788", "Av. A", 7500.0, c2)
p3.cadastrar()



# 04/04/2022
from Categoria import Categoria
from Produto import Produto

print("\n-------------04/04/2022 ----\n")

c1 = Categoria( 2 , "Bebidas")
p1 = Produto( 1, "Coca-Cola 2L", 7.99 , 50, c1)
p1.cadastrar()


p2 = Produto()

p2.setCategoria()

p2.cadastrar()

c2 = Categoria()
c3 = Categoria()