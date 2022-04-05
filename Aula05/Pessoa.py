class Pessoa:

	def __init__(self, nome = "Sem Nome", fone = "1234"):
		self.nome = nome
		self.telefone = fone

	def __str__(self):
		return "Name: " + self.nome + "\nPhone: " + self.telefone 
	