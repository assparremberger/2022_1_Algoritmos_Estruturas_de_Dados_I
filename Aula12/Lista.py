from No import No

class Lista:

	def __init__(self) :
		self.primeiro = None
		self.tamanho = 0

	def adicionar(self, valor) :
		nodo = No(valor)
		if self.primeiro == None:
			self.primeiro = nodo
		else:
			aux = self.primeiro
			
			while( aux.proximo ) :
				aux = aux.proximo
			
			aux.proximo = nodo
		self.tamanho += 1

	def imprimir(self) :
		if self.primeiro == None:
			print("A lista encadeada está vazia!")
		else:
			print("\n---------------------\n")
			aux = self.primeiro
			while( aux  ) :
				print( aux.dado , "\n" )
				aux = aux.proximo
			print("Tamanho da lista: ", self.tamanho)

	def excluir(self, valor) :
		tamanhoAnterior = self.tamanho
		if self.tamanho == 0:
			print("A lista encadeada está vazia!")
		elif self.tamanho == 1 :
			if self.primeiro.dado == valor:
				self.primeiro = None
				self.tamanho -= 1
#			else:
#				print("Valor não encontrado")
		else: 
			aux = self.primeiro
			if aux.dado == valor:
					# .   = self.primeiro.proximo
				self.primeiro = aux.proximo
				self.tamanho -= 1
			else:
				anterior = self.primeiro
				aux = self.primeiro.proximo
				while( aux ) :
					if aux.dado == valor:
						anterior.proximo = aux.proximo
						self.tamanho -= 1
					else:
						anterior = aux
					aux = aux.proximo	
		if tamanhoAnterior == self.tamanho:
			print( "Valor não encontrado")



		
