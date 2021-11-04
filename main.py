# EXERCICIO
# CRIAR UM SOFTAWARE DE GERENCIAMENTO BANCARIO
# ESSE SOFTAWARE SERA CAPAZ DE CRIAR CLIENTES E CONTAS, CADA CLIENTE POSSUE NOME, CPF , IDADE
# CADA CONTA POSSUE UM CLIENTE, E POSSUE UM SALDO E UM LIMITE, E TEM OS METODOS SACAR E DEPOSITAR E CONSULTAR SALDO

from cliente import Cliente
from conta import Conta
cliente1 = Cliente('Renan', '123456789-10', 22) # Criamos a conta que recebe a classe cliente, e jogamos dentro de cliente1

conta_renan = Conta(cliente1,100,200) # Aqui vamos definir a quem pertence a conta cliente1, que nesse caso e o Renan. A class Conta recebe 2 parametros ( Cliente, Saldo )


conta_renan.sacar(50)

conta_renan.depositar(100)

conta_renan.sacar(2500)












