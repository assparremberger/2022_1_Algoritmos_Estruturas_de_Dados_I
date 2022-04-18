from Pessoa import Pessoa
class Fisica(Pessoa):

	def __init__(self, nomeF , idadeF):
		super().__init__(nomeF)
		self.idade = idadeF
		#print("Pessoa Física construída")

	def __str__(self):
		return super().__str__() + "\nIdade:" +  str(self.idade) 

#	def imprimir(self):
#		print("Nome da P. Física: ", self.nome)
#		print("Telefone: ", self.telefone)
#		print("Idade: ", self.idade)

	def imprimir(self):
		Pessoa.imprimir(self)
		print("Idade: ", self.idade)