import pandas as pd
import re
import requests
import os
import teste2


cnpj = input ('Digite o CNPJ: ')

r = requests.get('https://minhareceita.org/{}'.format(cnpj))

data = r.json()

print ('CNPJ: {}'.format(data['cnpj']))
print ('Descrição Situação Cadastral: {}'.format (data['descricao_situacao_cadastral']))
print ('UF: {}'.format (data['uf']))
print ('Bairro: {}'.format(data['bairro']))
print ('Logradouro: {}'.format(data['logradouro']))
print ('Numero: {}'.format(data['numero']))
print ('Municipio: {}'.format(data['municipio']))
print ('Razão Social : {}'.format(data['razao_social']))





# 59531004000149