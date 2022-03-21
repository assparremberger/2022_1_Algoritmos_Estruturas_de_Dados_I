# Construir um algoritmo que contenha 3 listas, cada lista contendo:
# • Nomes de produtos
# • Preços de cada produto
# • Quantidades de cada produto
# • Construir uma função para imprimir um dos produtos da lista e uma 
# função para retirar um dos produtos das listas. As funções devem receber 
# um parâmetro que será usado para acessar a posição dos itens das listas 
# que serão impressos ou retirados.

#vet = [4 , 5 , 6]
#print( vet[-2] )

produtos = ["Coca-Cola" , "Pepsi", "Arroz"]
precos = [7.39 ,  5.99, 3.98]
quantidades = [100, 50, 30]


def imprimirTodos(  ):
	for i in range( len(produtos) ):
		print( "Nome: " , produtos[i] )
		print( "Preço: " , precos[i] )
		print( "Quantidade em estoque: " , quantidades[i] )
		print("---------------------")

def imprimir( posicao ):
	print( "Nome: " , produtos[posicao] )
	print( "Preço: " , precos[posicao] )
	print( "quantidade em estoque: " , quantidades[posicao] )

def excluir( posicao ):
	produtos.pop(posicao)
	precos.pop( posicao )
	quantidades.pop( posicao )

#excluir(2)
#imprimirTodos()	
print("1 - Imprimir um item da lista")
print("2 - excluir um item")
opcao = int( input("Informe sua opcao: "))
posicao = int( input("Informe a posição: "))
if opcao == 1 :
	imprimir(posicao)
elif opcao == 2: 
	excluir(posicao)
	imprimirTodos()
else: 
	print("Opão inválida!") 		


