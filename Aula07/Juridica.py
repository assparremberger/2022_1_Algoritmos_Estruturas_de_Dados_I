from Pessoa import Pessoa

class Juridica(Pessoa):

	def __init__(self, nome, cnpj ,fone="1234567890", nFuncionarios=0):
		super().__init__(nome, fone )
		self.cnpj = cnpj
		self.nFuncionarios = nFuncionarios

	def __str__(self):
		texto =  "\nCNPJ: " + self.cnpj + "\nFuncionários: " + str(self.nFuncionarios)	
		return super().__str__() + texto