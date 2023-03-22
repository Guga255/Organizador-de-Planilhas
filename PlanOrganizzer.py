import pandas as pd
import re
import requests

l_cnpj = []
l_dsc = []
l_uf = []
l_bairro = []
l_logra = []
l_num = []
l_muni = []
l_razao = []
l_telefone = []


df = pd.read_excel(r'C:\Users\User\Desktop\excel\Tabela de Clientes - DI SIENA = 17-01-2023.xlsx')

lista = []

for cnpj in df['cnpj']:
    lista.append(cnpj)

n_lista = []

for cnpj in lista:
    n_cnpj = re.sub(r'[^0-9]','',str(cnpj))
    n_lista.append(n_cnpj)

for cnpj in n_lista:
    if cnpj == '':
        n_lista.remove(cnpj)

for cnpj in n_lista:

    try:
        r = requests.get('https://minhareceita.org/{}'.format(cnpj))

        data = r.json()


        l_cnpj.append(data['cnpj'])
        l_dsc.append(data['descricao_situacao_cadastral'])
        l_uf.append(data['uf'])
        l_bairro.append(data['bairro'])
        l_logra.append(data['logradouro'])
        l_num.append(data['numero'])
        l_muni.append(data['municipio'])
        l_razao.append(data['razao_social'])
        l_telefone.append(data['ddd_telefone_1'])
    
    except:
        pass



    

excel = {'CNPJ': l_cnpj, 'Situação Cadastral': l_dsc, 'UF': l_uf, 'Bairro':l_bairro,'Logradouro': l_logra, 'Número': l_num, 'Município': l_muni, 'Razão Social': l_razao, 'Telefone': l_telefone}

df1 = pd.DataFrame (excel, columns=['CNPJ', 'Situação Cadastral', 'UF', 'Bairro', 'Logradouro', 'Número', 'Município', 'Razão Social', 'Telefone'])

df1.to_excel(r'C:\Users\User\Desktop\excel\Clientes CNPJ.xlsx', index=False)