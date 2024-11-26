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
