class Cliente:

	def __init__(self, nome = None, idade = 18 ):
		self.nome = nome
		self.idade = idade
		self.proximo = None

	def __str__(self) -> str:
		texto = "Nome: " + self.nome
		texto += "\nIdade: " + str(self.idade)
		if self.proximo == None:
			texto +=  "\nPróximo da fila: Não tem"
		else:
			texto +=  "\nPróximo da fila: " + self.proximo.nome
		return texto