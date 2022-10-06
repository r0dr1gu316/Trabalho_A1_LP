import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re

# Primeira Parte: Montando lista de músicas por ordem de mais ouvidas
# Trocando o user-agent fingindo ser um navegador para não ser impedido de coletar os dados da página e adquirindo o html bruto da página através da função requests.get
user = {"user-agent": "Mozilla/5.0"}

link1 = requests.get('https://pt.wikipedia.org/wiki/Transpira%C3%A7%C3%A3o_Cont%C3%ADnua_Prolongada',
                     headers=user)
html_bruto = link1.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

# Buscando as músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador
lista_album_transp = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

# Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem = []
for musica in lista_album_transp:
    nome_musica = musica.text
    musicas_ordem.append(nome_musica)


musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
del musicas_ordem [16:]

print(musicas_ordem)


duracao_album_transp = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem_duracao = []
for musica in duracao_album_transp:
    nome_musica = musica.text
    musicas_ordem_duracao.append(nome_musica)


musicas_ordem_duracao = [item.replace("\xa0", "") for item in musicas_ordem_duracao]
musicas_ordem_duracao = [item.replace("\n", "") for item in musicas_ordem_duracao]
musicas_ordem_duracao = [item.replace('"', "") for item in musicas_ordem_duracao]
del musicas_ordem_duracao [32:]

del musicas_ordem_duracao[::2]
print(musicas_ordem_duracao)


##############################
link2 = requests.get('https://pt.wikipedia.org/wiki/Pre%C3%A7o_Curto..._Prazo_Longo',
                     headers=user)
html_bruto = link2.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_preco = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem2 = []
for musica in lista_album_preco:
    nome_musica2 = musica.text
    musicas_ordem2.append(nome_musica2)
#print(musicas_ordem2)

musicas_ordem2 = [item.replace("\xa0", "") for item in musicas_ordem2]
musicas_ordem2 = [item.replace("\n", "") for item in musicas_ordem2]
musicas_ordem2 = [item.replace('"', "") for item in musicas_ordem2]

print(musicas_ordem2)

duracao_preco = html_arrumado.find_all('td',
                                           {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})
del musicas_ordem2[::2]

musicas_ordem2 = []
for musica in duracao_preco:
    nome_musica2 = musica.text
    musicas_ordem2.append(nome_musica2)
del musicas_ordem2[::2]
print(musicas_ordem2)

#################################

user = {"user-agent": "Mozilla/5.0"}

link3 = requests.get('https://pt.wikipedia.org/wiki/Nadando_com_os_Tubar%C3%B5es',
                     headers=user)
html_bruto = link3.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_nadando = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem3 = []
for musica in lista_album_nadando:
    nome_musica3 = musica.text
    musicas_ordem3.append(nome_musica3)

musicas_ordem3 = [item.replace("\xa0", "") for item in musicas_ordem3]
musicas_ordem3 = [item.replace("\n", "") for item in musicas_ordem3]
musicas_ordem3 = [item.replace('"', "") for item in musicas_ordem3]

print(musicas_ordem3)

duracao_nadando = html_arrumado.find_all('td',
                                             {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem3 = []
for musica in duracao_nadando:
    nome_musica3 = musica.text
    musicas_ordem3.append(nome_musica3)
del musicas_ordem3[::2]
print(musicas_ordem3)
#######################
user = {"user-agent": "Mozilla/5.0"}

link4 = requests.get('https://pt.wikipedia.org/wiki/100%25_Charlie_Brown_Jr._-_Abalando_a_Sua_F%C3%A1brica',
                     headers=user)
html_bruto = link4.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_abalando = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem4 = []
for musica in lista_album_abalando:
    nome_musica4 = musica.text
    musicas_ordem4.append(nome_musica4)

musicas_ordem4 = [item.replace("\xa0", "") for item in musicas_ordem4]
musicas_ordem4 = [item.replace("\n", "") for item in musicas_ordem4]
musicas_ordem4 = [item.replace('"', "") for item in musicas_ordem4]

print(musicas_ordem4)

duracao_abalando = html_arrumado.find_all('td',
                                              {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem4 = []
for musica in duracao_abalando:
    nome_musica4 = musica.text
    musicas_ordem4.append(nome_musica4)
del musicas_ordem4[::2]
print(musicas_ordem4)

###############################

link5 = requests.get('https://pt.wikipedia.org/wiki/Bocas_Ordin%C3%A1rias',
                     headers=user)
html_bruto = link5.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_bocas = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem5 = []
for musica in lista_album_bocas:
    nome_musica5 = musica.text
    musicas_ordem5.append(nome_musica5)

musicas_ordem5 = [item.replace("\xa0", "") for item in musicas_ordem5]
musicas_ordem5 = [item.replace("\n", "") for item in musicas_ordem5]
musicas_ordem5 = [item.replace('"', "") for item in musicas_ordem5]

print(musicas_ordem5)

duracao_bocas = html_arrumado.find_all('td',{'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem5 = []
for musica in duracao_bocas:
    nome_musica5 = musica.text
    musicas_ordem5.append(nome_musica5)
del musicas_ordem5[::2]
print(musicas_ordem5)

#################################
link6 = requests.get('https://pt.wikipedia.org/wiki/Tamo_A%C3%AD_na_Atividade',
                     headers=user)
html_bruto = link6.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_tamoai = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem6 = []
for musica in lista_album_tamoai:
    nome_musica6 = musica.text
    musicas_ordem6.append(nome_musica6)

musicas_ordem6 = [item.replace("\xa0", "") for item in musicas_ordem6]
musicas_ordem6 = [item.replace("\n", "") for item in musicas_ordem6]
musicas_ordem6 = [item.replace('"', "") for item in musicas_ordem6]

print(musicas_ordem6)

duracao_tamoai = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem6 = []
for musica in duracao_tamoai:
    nome_musica6 = musica.text
    musicas_ordem6.append(nome_musica6)
del musicas_ordem6[::2]
print(musicas_ordem6)

###############################
link7 = requests.get('https://pt.wikipedia.org/wiki/Imunidade_Musical',
                     headers=user)
html_bruto = link7.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_imunidade = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem7 = []
for musica in lista_album_imunidade:
    nome_musica7 = musica.text
    musicas_ordem7.append(nome_musica7)

musicas_ordem7 = [item.replace("\xa0", "") for item in musicas_ordem7]
musicas_ordem7 = [item.replace("\n", "") for item in musicas_ordem7]
musicas_ordem7 = [item.replace('"', "") for item in musicas_ordem7]

print(musicas_ordem7)

duracao_imunidade = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem7 = []
for musica in duracao_imunidade:
    nome_musica7 = musica.text
    musicas_ordem7.append(nome_musica7)
del musicas_ordem7[::2]
print(musicas_ordem7)

###############################
link8 = requests.get('https://pt.wikipedia.org/wiki/Ritmo,_Ritual_e_Responsa',
                     headers=user)
html_bruto = link8.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_ritmo = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem8 = []
for musica in lista_album_ritmo:
    nome_musica8 = musica.text
    musicas_ordem8.append(nome_musica8)

musicas_ordem8 = [item.replace("\xa0", "") for item in musicas_ordem8]
musicas_ordem8 = [item.replace("\n", "") for item in musicas_ordem8]
musicas_ordem8 = [item.replace('"', "") for item in musicas_ordem8]

print(musicas_ordem8)

duracao_ritmo = html_arrumado.find_all('td',
                                           {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem8 = []
for musica in duracao_ritmo:
    nome_musica8 = musica.text
    musicas_ordem8.append(nome_musica8)
del musicas_ordem8[::2]
print(musicas_ordem8)

########################################
link9 = requests.get('https://pt.wikipedia.org/wiki/Camisa_10_Joga_Bola_At%C3%A9_na_Chuva',
                     headers=user)
html_bruto = link9.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_camisa = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem9 = []
for musica in lista_album_camisa:
    nome_musica9 = musica.text
    musicas_ordem9.append(nome_musica9)

musicas_ordem9 = [item.replace("\xa0", "") for item in musicas_ordem9]
musicas_ordem9 = [item.replace("\n", "") for item in musicas_ordem9]
musicas_ordem9 = [item.replace('"', "") for item in musicas_ordem9]

print(musicas_ordem9)

duracao_camisa = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem9 = []
for musica in duracao_camisa:
    nome_musica9 = musica.text
    musicas_ordem9.append(nome_musica9)
del musicas_ordem9[::2]
print(musicas_ordem9)

###################################
link10 = requests.get('https://pt.wikipedia.org/wiki/La_Familia_013',
                      headers=user)
html_bruto = link10.text
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

lista_album_013 = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})

musicas_ordem10 = []
for musica in lista_album_013:
    nome_musica10 = musica.text
    musicas_ordem10.append(nome_musica10)

musicas_ordem10 = [item.replace("\xa0", "") for item in musicas_ordem10]
musicas_ordem10 = [item.replace("\n", "") for item in musicas_ordem10]
musicas_ordem10 = [item.replace('"', "") for item in musicas_ordem10]

print(musicas_ordem10)

duracao_013 = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})

musicas_ordem10 = []
for musica in duracao_013:
    nome_musica10 = musica.text
    musicas_ordem10.append(nome_musica10)
del musicas_ordem10[::2]
print(musicas_ordem10)
