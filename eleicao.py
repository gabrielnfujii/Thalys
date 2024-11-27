import tkinter as tk
from tkinter import messagebox
import csv
import pickle
import os

def carregar_csv(arquivo):
    dados = []
    try:
        with open(arquivo, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                dados.append(linha)
    except FileNotFoundError:
        messagebox.showerror("Erro", f"Arquivo {arquivo} não encontrado.")
    return dados

def salvar_votos(arquivo, votos):
    with open(arquivo, 'wb') as f:
        pickle.dump(votos, f)

def carregar_votos(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    return []

class UrnaEletronica:
    def __init__(self, root):
        self.root = root
        self.root.title("Urna Eletrônica")
        

        self.eleitores = carregar_csv('eleitores.csv')
        self.candidatos = carregar_csv('candidatos.csv')
        self.votos = carregar_votos('votos.pkl')
        self.eleitor_atual = None


        self.tela_inicial()

    def tela_inicial(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Digite o número do título de eleitor:").pack(pady=10)
        self.titulo_entry = tk.Entry(self.root)
        self.titulo_entry.pack(pady=5)
        tk.Button(self.root, text="Verificar", command=self.verificar_eleitor).pack(pady=10)

    def verificar_eleitor(self):
        titulo = self.titulo_entry.get()
        eleitor = next((e for e in self.eleitores if e['titulo'] == titulo), None)
        
        if eleitor:
            if any(v['titulo'] == titulo for v in self.votos):
                messagebox.showinfo("Atenção", "Este eleitor já votou.")
                self.tela_inicial()
            else:
                self.eleitor_atual = eleitor
                self.tela_votacao()
        else:
            messagebox.showerror("Erro", "Eleitor não encontrado.")
            self.tela_inicial()

    def tela_votacao(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text=f"Bem-vindo, {self.eleitor_atual['nome']}!").pack(pady=10)
        tk.Label(self.root, text="Digite o número do candidato ou escolha outra opção:").pack(pady=10)
        
        self.voto_entry = tk.Entry(self.root)
        self.voto_entry.pack(pady=5)
        
        tk.Button(self.root, text="Confirmar", command=self.registrar_voto).pack(pady=5)
        tk.Button(self.root, text="Voto Branco", command=lambda: self.registrar_voto(voto="branco")).pack(pady=5)
        tk.Button(self.root, text="Voto Nulo", command=lambda: self.registrar_voto(voto="nulo")).pack(pady=5)

    def registrar_voto(self, voto=None):
        if voto is None:
            numero_candidato = self.voto_entry.get()
            candidato = next((c for c in self.candidatos if c['numero'] == numero_candidato), None)
            if candidato:
                voto = candidato['nome']
            else:
                voto = "nulo"
        
        self.votos.append({'titulo': self.eleitor_atual['titulo'], 'voto': voto})
        salvar_votos('votos.pkl', self.votos)
        messagebox.showinfo("Sucesso", "Voto registrado com sucesso!")
        self.tela_inicial()

if __name__ == "__main__":
    root = tk.Tk()
    urna = UrnaEletronica(root)
    root.mainloop()
