def getTamanho(x):
	return len(x)

def aumentarPreco( p ):
	return p * 1.1

frutas = "Laranja", "Banana", "Limão"

tamanhos = map( getTamanho , frutas )
print( list(tamanhos) )

precos = [ 6.0 , 10.5 , 20.3, 100 ]

novosPrecos = map( aumentarPreco , precos )
print( list( novosPrecos ))

produtos = {
	0: 10.0 ,
	8: 8.99 ,
	2: 6.79
}
novosPrecosProdutos = map( aumentarPreco, produtos )
print( list( novosPrecosProdutos ) )