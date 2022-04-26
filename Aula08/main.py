from Conta import Conta

c1 = Conta()

c1.imprimirSaldo()

c1.depositar( 25 )

c1.imprimirSaldo()

c1.sacar( 10 )

c1.imprimirSaldo()

#c1.__descontarTarifa()

c1.setSaldo( 100 )

c1.imprimirSaldo()

#print( str( c1.getSaldo() * 2) )
print("\n-----------------\n\n")
print( str( c1.saldo * 2) )

c1.saldo = 20
c1.imprimirSaldo()