import pandas as pd
import os

# Nome do arquivo onde as indicações serão armazenadas
arquivo_excel = "indicacoes.xlsx"

def capturar_dados():
    """Captura os dados da indicação via input do usuário."""
    responsavel = input("Nome do responsável: ").strip()
    numero = input("Número: ").strip()
    contabilidade = input("Nome da contabilidade: ").strip()
    indicado_por = input("Nome da contabilidade que indicou: ").strip()
    
    return {"Responsável": responsavel, "Número": numero, "Contabilidade": contabilidade, "Indicado Por": indicado_por}

def salvar_no_excel(dados):
    """Salva os dados capturados no arquivo Excel."""
    try:
        # Se o arquivo já existe, carrega os dados existentes
        df = pd.read_excel(arquivo_excel)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Responsável", "Número", "Contabilidade", "Indicado Por"])
    
    # Adiciona a nova entrada
    df = df.append(dados, ignore_index=True)
    
    # Salva no Excel
    df.to_excel(arquivo_excel, index=False)
    print("\n✅ Indicação salva com sucesso!")

def commit_e_push():
    """Atualiza o arquivo no GitHub automaticamente."""
    os.system("git add indicacoes.xlsx")
    os.system('git commit -m "Atualizando lista de indicações"')
    os.system("git push origin main")
    print("\n🚀 Arquivo atualizado no GitHub!")

if __name__ == "__main__":
    dados = capturar_dados()
    salvar_no_excel(dados)
    commit_e_push()
