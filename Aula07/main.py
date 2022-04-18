from Juridica import Juridica
from Pessoa import Pessoa
from Fisica import Fisica

p1 = Pessoa("João", "(51) 2233-4455")
#print( p1 )

pf = Fisica( "José da Silva" , 20 )
print( pf )

pj = Juridica("Jõao da Silva ME.","00.111.222/0001-33", "3322-4455")
#print("Nome: ", pj.nome)
print("-----------")
print(pj)


p2 = Pessoa("Maria")
p3 = Pessoa("Carlos", 12345.0 )


print( "\n-----------------------------\n\n")

pf1 = Fisica("Adalto", 36)
pf1.telefone = "(51) 98765-4321"

pf1.imprimir()



