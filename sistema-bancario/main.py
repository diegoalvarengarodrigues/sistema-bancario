from model.caixa_eletronico import CaixaEletronico
from view.tela_caixa_eletronico import TelaCaixaEletronico
from controller.controller import Controller

if __name__ == "__main__":
    caixa_eletronico = CaixaEletronico()
    tela_caixa_eletronico = TelaCaixaEletronico(caixa_eletronico)
    controller = Controller(caixa_eletronico, tela_caixa_eletronico)
    
    tela_caixa_eletronico.mainloop()