
# Sistema de Votação Eletrônica - Curso de Sistemas de Informação

Este repositório contém um sistema de votação eletrônica desenvolvido como parte de uma atividade acadêmica no curso de Sistemas de Informação da Universidade Católica de Santos.  

## Membros do Projeto
- Felipe Shinzato  
- Gabriel Fujii  
- Daniel Thalys  
- Breno Severino  

---

## Objetivo do Projeto
O sistema simula um processo de votação eletrônica, permitindo que eleitores cadastrados escolham candidatos registrados. Ele inclui funcionalidades para carregar e salvar dados, bem como gerenciar votos.

---

## Arquivos no Repositório
1. **`README.md`**: Este arquivo de documentação.  
2. **`eleicao.py`**: O código principal do sistema, que utiliza a biblioteca `tkinter` para criar a interface gráfica. Ele também contém funções para carregar e salvar dados usando arquivos CSV e serialização com `pickle`.  
3. **`candidatos.csv`**: Arquivo CSV contendo a lista de candidatos disponíveis na eleição, com detalhes como nome e número.  
4. **`eleitores.csv`**: Arquivo CSV contendo informações dos eleitores cadastrados, como CPF e nome.

---

## Estrutura do Sistema
O sistema foi desenvolvido em Python e utiliza:
- **`tkinter`** para interface gráfica com o usuário.
- **`csv`** para manipulação de arquivos de dados (candidatos e eleitores).
- **`pickle`** para salvar e carregar votos em formato binário.
- **Gerenciamento de arquivos** para garantir persistência dos dados.

### Funcionalidades Principais
1. **Carregar dados**: Lê os arquivos CSV de candidatos e eleitores.  
2. **Registrar votos**: Permite que eleitores votem nos candidatos disponíveis.  
3. **Salvar votos**: Armazena os votos de maneira segura utilizando `pickle`.  
4. **Carregar votos**: Recupera os votos previamente salvos.

---

## Como Usar
### Pré-requisitos
1. Python 3.10 ou superior instalado.  
2. Certifique-se de que os arquivos `candidatos.csv` e `eleitores.csv` estejam na mesma pasta que o script `eleicao.py`.

### Passo a Passo
1. **Baixe os arquivos do repositório**.  
2. **Configure os arquivos CSV**:  
   - **`candidatos.csv`**: Preencha com os candidatos e seus números.  
   - **`eleitores.csv`**: Adicione os eleitores autorizados a votar.  
3. **Execute o script principal**:  
   ```bash
   python eleicao.py
   ```
4. **Interaja com a interface gráfica**:  
   - Escolha o eleitor e o candidato.  
   - Submeta o voto.  

### Exemplo de Conteúdo dos Arquivos CSV
**`candidatos.csv`**:
```csv
numero,nome
1,Fernando Silva
2,Joana Oliveira
```

**`eleitores.csv`**:
```csv
cpf,nome
12345678901,José Santos
10987654321,Maria Lima
```

---

## Observações
- Certifique-se de que todos os arquivos necessários estejam no formato correto.  
- O sistema exibirá mensagens de erro caso algum arquivo esteja faltando ou incorreto.  

---
