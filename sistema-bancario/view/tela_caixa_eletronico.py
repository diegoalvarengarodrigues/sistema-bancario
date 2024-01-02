import tkinter as tk
from tkinter import messagebox

class TelaCaixaEletronico(tk.Tk):
    def __init__(self, caixa_eletronico):
        super().__init__()
        self.caixa_eletronico = caixa_eletronico
        self.title("Caixa Eletrônico")
        self.geometry("400x300")

        self.label_bem_vindo = tk.Label(self, text="Bem-vindo ao Caixa Eletrônico", font=("Arial", 16))
        self.label_bem_vindo.pack(pady=20)

        self.botao_deposito = tk.Button(self, text="Depósito", command=self.tela_deposito)
        self.botao_saque = tk.Button(self, text="Saque", command=self.tela_saque)
        self.botao_extrato = tk.Button(self, text="Extrato", command=self.exibir_extrato)
        self.botao_sair = tk.Button(self, text="Sair", command=self.quit)

        self.botao_deposito.pack(side=tk.LEFT, padx=20)
        self.botao_saque.pack(side=tk.LEFT, padx=20)
        self.botao_extrato.pack(side=tk.LEFT, padx=20)
        self.botao_sair.pack(side=tk.LEFT, padx=20)

    def tela_deposito(self):
        self.limpar_tela()
        self.label_operacao = tk.Label(self, text="Depósito", font=("Arial", 14))
        self.label_operacao.pack(pady=10)

        self.label_instrucao = tk.Label(self, text="Digite o valor a ser depositado:")
        self.label_instrucao.pack()

        self.valor_var = tk.StringVar()
        self.entry_valor = tk.Entry(self, textvariable=self.valor_var)
        self.entry_valor.pack(pady=10)

        self.botao_finalizar = tk.Button(self, text="Finalizar Depósito", command=self.finalizar_deposito)
        self.botao_finalizar.pack(pady=10)

    def finalizar_deposito(self):
        try:
            valor = float(self.valor_var.get())
            mensagem = self.caixa_eletronico.deposito(valor)
            messagebox.showinfo("Depósito", mensagem)
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")
        finally:
            self.recriar_tela_inicial()

    def tela_saque(self):
        self.limpar_tela()
        self.label_operacao = tk.Label(self, text="Saque", font=("Arial", 14))
        self.label_operacao.pack(pady=10)

        self.label_instrucao = tk.Label(self, text="Digite o valor a ser sacado:")
        self.label_instrucao.pack()

        self.valor_var = tk.StringVar()
        self.entry_valor = tk.Entry(self, textvariable=self.valor_var)
        self.entry_valor.pack(pady=10)

        self.botao_finalizar = tk.Button(self, text="Finalizar Saque", command=self.finalizar_saque)
        self.botao_finalizar.pack(pady=10)

    def finalizar_saque(self):
        try:
            valor = float(self.valor_var.get())
            mensagem = self.caixa_eletronico.saque(valor)
            messagebox.showinfo("Saque", mensagem)
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")
        finally:
            self.recriar_tela_inicial()

    def exibir_extrato(self):
        mensagem = self.caixa_eletronico.extrato()
        messagebox.showinfo("Extrato", mensagem)

    def limpar_tela(self):
        for widget in self.winfo_children():
            widget.destroy()

    def criar_botoes(self):
        self.botao_deposito = tk.Button(self, text="Depósito", command=self.tela_deposito)
        self.botao_saque = tk.Button(self, text="Saque", command=self.tela_saque)
        self.botao_extrato = tk.Button(self, text="Extrato", command=self.exibir_extrato)
        self.botao_sair = tk.Button(self, text="Sair", command=self.quit)

        self.botao_deposito.pack(side=tk.LEFT, padx=20)
        self.botao_saque.pack(side=tk.LEFT, padx=20)
        self.botao_extrato.pack(side=tk.LEFT, padx=20)
        self.botao_sair.pack(side=tk.LEFT, padx=20)
        
    def configure_botoes(self, deposito, saque, extrato, sair):
        self.botao_deposito.configure(command=deposito)
        self.botao_saque.configure(command=saque)
        self.botao_extrato.configure(command=extrato)
        self.botao_sair.configure(command=sair)
        
    def recriar_tela_inicial(self):
        # Destruir os widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        # Recriar a tela inicial
        self.label_bem_vindo = tk.Label(self, text="Bem-vindo ao Caixa Eletrônico", font=("Arial", 16))
        self.label_bem_vindo.pack(pady=20)

        self.criar_botoes()