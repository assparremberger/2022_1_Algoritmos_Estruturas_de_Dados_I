from No import No
#Lista duplamente encadeada
class Lista:

	def __init__(self) :
		self.primeiro = None
		self.ultimo = None
		self.tamanho = 0

	def adicionarNoInicio(self, valor) :
		nodo = No(valor)
		if self.primeiro == None:
			self.ultimo = nodo
		else:
			self.primeiro.anterior = nodo
			nodo.proximo = self.primeiro
		self.primeiro = nodo
		self.tamanho += 1

	def adicionarNoFim(self, valor) :
		nodo = No(valor)
		if self.primeiro == None:
			self.primeiro = nodo
		else:
			self.ultimo.proximo = nodo
			nodo.anterior = self.ultimo
		self.ultimo = nodo
		self.tamanho += 1

	

	def imprimir(self) :
		if self.primeiro == None:
			print("A lista duplamente encadeada está vazia!")
		else:
			print("\n---------------------\n")
			aux = self.primeiro
			while( aux  ) :
				print( aux.dado , "\n" )
				aux = aux.proximo
			print("Tamanho da lista: ", self.tamanho)

	
	def imprimirReverso(self) :
		if self.primeiro == None:
			print("A lista duplamente encadeada está vazia!")
		else:
			print("\n---------------------\n")
			aux = self.ultimo
			while( aux  ) :
				print( aux.dado , "\n" )
				aux = aux.anterior
			print("Tamanho da lista: ", self.tamanho)






	def excluir(self, valor) :
		tamanhoAnterior = self.tamanho
		if self.tamanho == 0:
			print("A lista duplamente encadeada está vazia!")
		elif self.tamanho == 1 :
			if self.primeiro.dado == valor:
				self.primeiro = None
				self.ultimo = None
				self.tamanho -= 1
		else: 
			aux = self.primeiro
			if aux.dado == valor:
				self.primeiro = aux.proximo
				self.primeiro.anterior = None
				self.tamanho -= 1
			else:
				ant = self.primeiro
				aux = self.primeiro.proximo
				while( aux ) :
					if aux.dado == valor:
						ant.proximo = aux.proximo
						aux.proximo.anterior = ant
						self.tamanho -= 1
					else:
						ant = aux
					aux = aux.proximo	
		if tamanhoAnterior == self.tamanho:
			print( "Valor não encontrado")

	def excluirDoInicio(self):
		if self.primeiro == None:
			print( "A lista duplamente encadeada está vazia!")
		elif self.primeiro == self.ultimo:
			self.primeiro = None
			self.ultimo = None
			self.tamanho = 0
		else:
			self.primeiro = self.primeiro.proximo
			self.primeiro.anterior = None
			self.tamanho -= 1

	def excluirDoFim(self):
		if self.primeiro == None:
			print( "A lista duplamente encadeada está vazia!")
		elif self.primeiro == self.ultimo:
			self.primeiro = None
			self.ultimo = None
			self.tamanho = 0
		else:
			self.ultimo = self.ultimo.anterior
			self.ultimo.proximo = None
			self.tamanho -= 1


		
