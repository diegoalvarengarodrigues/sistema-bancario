class CaixaEletronico:
    def __init__(self, saldo_inicial=1000, saques_diarios=3, limite_saque=500):
        self.saldo_inicial = saldo_inicial
        self.saldo = saldo_inicial
        self.saques_diarios = saques_diarios
        self.limite_saque = limite_saque
        self.saques_feitos = 0
        self.operacoes = []
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(
            f'Depósito de R${valor:.2f}. Saldo: R${self.saldo:.2f}')
        return f'Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}'

    def saque(self, valor):
        if valor > self.saldo or valor > self.limite_saque or self.saques_feitos >= self.saques_diarios:
            return 'Erro: Saque não permitido.'

        self.saldo -= valor
        self.saques_feitos += 1
        self.operacoes.append(
            f'Saque de R${valor:.2f}. Saldo: R${self.saldo:.2f}')
        return f'Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}'

    def extrato(self):
        extrato = f'Saldo Inicial: R${self.saldo_inicial:.2f}\n'
        for op in self.operacoes:
            extrato += op + '\n'
        return extrato