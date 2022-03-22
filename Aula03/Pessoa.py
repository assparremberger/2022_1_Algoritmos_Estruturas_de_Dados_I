class Pessoa:

	def __init__(self, nomeP = None , fone = None, salarioP = 1212.00):
		self.nome = nomeP
		self.telefone = fone
		self.salario = salarioP
		#print("Objeto construído!")



print("--------")
p1 = Pessoa()
print("O nome da pessoa é: ", p1.nome)
print("O telefone da pessoa é: ", p1.telefone)
print("O slário da pessoa é: ", p1.salario)

##print("Valor é: ", p1)