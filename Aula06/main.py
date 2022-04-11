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