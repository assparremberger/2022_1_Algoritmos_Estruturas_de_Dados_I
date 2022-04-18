class Pessoa:

	def __init__(self, nome, fone = "1234567890"):
		self.nome = nome
		self.telefone = fone

	def __str__(self):
		return "Nome: " + self.nome + "\nPhone: " + self.telefone 
	

	def imprimir(self):
		print("Nome: ", self.nome)
		print("Fone: ", self.telefone)
