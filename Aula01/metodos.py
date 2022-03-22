# método que não recebe parâmetro e tem retorno
def getPi():
	return 3.14

# método que não recebe parâmetro e não retorna nada
def imprimirPi( ):
	print( "O valor de PI é: " , getPi() )

# Método que recebe parâmetro e tem retorno
def calcularAreaCirculo(raio):
	area = getPi() * ( raio * raio )
	return area

# Método que recebe parâmetro e não tem retorno
def imprimirAreaDoCirculo(r):
	print( "A área do circulo com raio ", r , " é: " ,calcularAreaCirculo(raio=r) )


def calcularArea(largura , comprimento):
	area = float(largura) * float(comprimento)
	return area


# bloco de execução
# print( "O valor de PI é: " , getPi() )
# imprimirPi()
# print( "A área do circulo com raio 3 é: " , calcularAreaCirculo( 3 ) )
imprimirAreaDoCirculo(4)

print( "Área total: " , calcularArea( "3", 3.5) )

