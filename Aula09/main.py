from Veiculo import Veiculo
from Carro import Carro
# Não podemos instanciar um objeto de uma classe abstrata
# v = Veiculo()

c = Carro("Doblo", 2006, 4)
c.imprimir()
print("---------")
c.imprimirEspecifico()
