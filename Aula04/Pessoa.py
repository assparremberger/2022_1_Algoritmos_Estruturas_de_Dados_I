class Pessoa:
	#salario = 1212.0

	def __init__(self, nomeP = None , fone = None, enderecoP = None, salarioP = 1212.0, cid = None):
		self.nome = nomeP
		self.telefone = fone
		self.endereco = enderecoP
		self.salario = salarioP
		self.municipio = cid

	def cadastrar(self):
		print("Nome: ", self.nome)
		print("Telefone: ", self.telefone )
		print("Salário: ", self.salario)
		print("Endereço: ", self.endereco)
		print("Cidade: ", self.municipio.nome, "/", self.municipio.estado)
		print( "Cadastrado com sucesso!")




