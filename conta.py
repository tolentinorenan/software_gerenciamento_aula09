class Conta:

    def __init__(self,cliente,saldo,limite):
        self.cliente= cliente
        self.saldo = saldo
        self.limite = 0 - limite  # numero negativo

    def depositar (self,quant):
        if quant >= 0:
            self.saldo += quant
            print('Você depositou o valor de R$', quant)
            print ('Saldo Atual R$', self.saldo)
        else:
            print ('Erro no deposito, valor inferior a 0')

    def sacar (self,quant):
        if self.saldo - quant < self.limite:
            print ('Voce nao tem dinheiro')
        else:
            self.saldo -= quant
            print ('Você sacou o valor de R$', quant)
            print('Saldo Atual R$', self.saldo)



