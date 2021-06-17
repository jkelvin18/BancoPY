from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity', 'felicity@email', '123.456.789-81', '02/09/1972')

jao: Cliente = Cliente('jao', 'felicity@email', '123.456.739-81', '02/09/1972')

print(felicity)

Contaf : Conta = Conta(felicity)
contae : Conta = Conta(jao)

print (Contaf)
print (contae)

