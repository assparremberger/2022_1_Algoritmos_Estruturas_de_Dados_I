from No import No
class Pilha:

	def __init__(self):
		self.topo = None
		self.tamanho = 0

	def adicionar(self, valor) :
		nodo = No(valor)
		if self.topo == None:
			self.topo = nodo
		else:
			nodo.proximo = self.topo	
			self.topo = nodo
		self.tamanho += 1
		self.imprimir()

	
	def imprimir(self) :
		if self.topo == None:
			print("A Pilha está vazia!")
		else:
			print("\n---------------------\n")
			aux = self.topo
			while( aux  ) :
				print( aux.dado , "\n" )
				aux = aux.proximo
			print("Tamanho da Pilha: ", self.tamanho)
	
	def remover(self):
		if self.topo == None:
			print("A Pilha está vazia!")
		elif self.topo.proximo == None:
			self.topo = None
			self.tamanho = 0
		else:
			self.topo = self.topo.proximo
			self.tamanho -= 1
		self.imprimir()