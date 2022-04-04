from Categoria import Categoria


class Produto:

	def __init__(self, cod = None, nomeP = None, precoP = 0.0, qtd = 0.0, catP = None):
		self.codigo = cod
		self.nome = nomeP
		self.preco = precoP
		self.quantidade = qtd
		self.cat = catP

	def cadastrar(self):
		print("Código: ", self.codigo)
		print("Nome: ", self.nome)
		print("Preço: ", self.preco)
		print("Quantidade: ", self.quantidade)
		print("Categoria: ", self.cat)
		print( "Produto cadastrado com sucesso!")

	def setCategoria(self, catP = Categoria() ):
		self.cat = catP

