class Controller:
    def __init__(self, caixa_eletronico, tela_caixa_eletronico):
        self.caixa_eletronico = caixa_eletronico
        self.tela_caixa_eletronico = tela_caixa_eletronico
        self.tela_caixa_eletronico.configure_botoes(self.tela_deposito, self.tela_saque, self.exibir_extrato, self.sair)

    def tela_deposito(self):
        self.tela_caixa_eletronico.tela_deposito()

    def tela_saque(self):
        self.tela_caixa_eletronico.tela_saque()

    def exibir_extrato(self):
        extrato = self.caixa_eletronico.extrato()
        self.tela_caixa_eletronico.mostrar_mensagem(extrato)

    def sair(self):
        self.tela_caixa_eletronico.encerrar()
