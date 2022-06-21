carro = { 
	"modelo" : "Doblo" , 
	"ano" : 2006 , 
	"reboque": False , 
	"capacidade": 950.243 
}


print( carro )

print( carro["ano"] )
print( carro["reboque"] )

print( carro.keys() )
print( carro.values() )

for chave, valor in carro.items():
	print( chave, "-" , valor)
print("----------------------")
for chave in carro.keys():
	print( chave, "-" , carro[chave])


filho1 = { "nome" : "Júlia" , "idade" : 13 }
filho2 = { "nome" : "Neimar" , "idade" : 5 }
filho3 = { "nome" : "Maria" , "idade" : 6 }



filhos = filho1, filho2
print( filhos )
#filhos[1] = filho3
filho1["email"] = "j@g.com"
filho2["nome"] = "Romario"
del filho1["idade"]
print( filhos )