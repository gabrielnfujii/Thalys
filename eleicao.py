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


