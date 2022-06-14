from Lista import Lista

lista = Lista()

lista.imprimir()

lista.adicionarNoInicio( "João")
lista.imprimir()

lista.adicionarNoInicio( "Maria")
lista.adicionarNoFim("José")

lista.adicionarNoFim("Carlos")
lista.adicionarNoInicio("Júlia")

lista.imprimir()
lista.imprimirReverso()

lista.excluir("José")
lista.imprimirReverso()

lista.excluirDoFim()
lista.excluirDoInicio()
lista.imprimir()




