import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

#Primeira Parte: Montando lista de músicas por ordem de mais ouvidas
#Trocando o user-agent fingindo ser um navegador para não ser impedido de coletar os dados da página e adquirindo o html bruto da página através da função requests.get
user = {"user-agent": "Mozilla/5.0"}
link1= requests.get('https://pt.wikipedia.org/wiki/Transpira%C3%A7%C3%A3o_Cont%C3%ADnua_Prolongada',
                       headers = user)
html_bruto = link1.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

#####################################
user = {"user-agent": "Mozilla/5.0"}
link2 = requests.get('https://pt.wikipedia.org/wiki/Pre%C3%A7o_Curto..._Prazo_Longo',
                       headers = user)
html_bruto = link2.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

#######################################
user = {"user-agent": "Mozilla/5.0"}
link3 = requests.get('https://pt.wikipedia.org/wiki/Nadando_com_os_Tubar%C3%B5es',
                       headers = user)
html_bruto = link3.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

#########################################
user = {"user-agent": "Mozilla/5.0"}
link4 = requests.get('https://pt.wikipedia.org/wiki/100%25_Charlie_Brown_Jr._-_Abalando_a_Sua_F%C3%A1brica',
                       headers = user)
html_bruto = link4.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')
############################################
user = {"user-agent": "Mozilla/5.0"}
link5 = requests.get('https://pt.wikipedia.org/wiki/Bocas_Ordin%C3%A1rias',
                       headers = user)
html_bruto = link5.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

###########################################
user = {"user-agent": "Mozilla/5.0"}
link6 = requests.get('https://pt.wikipedia.org/wiki/Tamo_A%C3%AD_na_Atividade',
                       headers = user)
html_bruto = link6.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

################################################
user = {"user-agent": "Mozilla/5.0"}
link7 = requests.get('https://pt.wikipedia.org/wiki/Imunidade_Musical',
                       headers = user)
html_bruto = link7.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

################################################
user = {"user-agent": "Mozilla/5.0"}
link8 = requests.get('https://pt.wikipedia.org/wiki/Ritmo,_Ritual_e_Responsa',
                       headers = user)
html_bruto = link8.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

#############################################
user = {"user-agent": "Mozilla/5.0"}
link9 = requests.get('https://pt.wikipedia.org/wiki/Camisa_10_Joga_Bola_At%C3%A9_na_Chuva',
                       headers = user)
html_bruto = link9.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

#################################################
user = {"user-agent": "Mozilla/5.0"}
link10 = requests.get('https://pt.wikipedia.org/wiki/La_Familia_013',
                       headers = user)
html_bruto = link10.text
#Arrumando o html com o html.parser
html_arrumado = BeautifulSoup(html_bruto, 'html.parser')

#----------------------------------------------------------
#ALBUM Transpiração Contínua Prolongada
lista_album_transp = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_transp)

#################ALBUM Preço Curto... Prazo Longo############################## 
lista_album_curto = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_curto)

###################ALBUM Nadando com os Tubarões############################
lista_album_nadando = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_nadando)

#################100% Charlie Brown Jr. - Abalando a Sua Fábrica############################### 
lista_album_abalando = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_abalando)

###################ALBUM Bocas Ordinárias############################
lista_album_bocas = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_bocas)

####################ALBUM Tamo Aí na Atividade########################### 
lista_album_tamo = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_tamo)

#####################ALBUM Imunidade Musical##########################
lista_album_imunidade = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_imunidade)

#################Ritmo, Ritual e Responsa############################### 
lista_album_ritmo = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_ritmo)

####################Camisa 10 Joga Bola Até na Chuva#############################
lista_album_camisa = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_camisa)
####################ALBUM La Familia 013##############################
lista_album_la = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})
print(lista_album_la)

#------------------------------------------------------

#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem = []
for musica in lista_album_transp:
   nome_musica = musica.text
   musicas_ordem.append(nome_musica)
print(musicas_ordem)

#################################
#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem2 = []
for musica in lista_album_curto:
   nome_musica2 = musica.text
   musicas_ordem2.append(nome_musica2)
print(musicas_ordem2)

##############################

#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem3 = []
for musica in lista_album_nadando:
   nome_musica3 = musica.text
   musicas_ordem3.append(nome_musica3)
print(musicas_ordem3)

####################################
#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem4 = []
for musica in lista_album_abalando:
   nome_musica4 = musica.text
   musicas_ordem4.append(nome_musica4)
print(musicas_ordem4)
#################################

#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem5 = []
for musica in lista_album_bocas:
   nome_musica5 = musica.text
   musicas_ordem5.append(nome_musica5)
print(musicas_ordem5)
##############################
musicas_ordem6 = []
for musica in lista_album_tamo:
   nome_musica6 = musica.text
   musicas_ordem6.append(nome_musica6)
print(musicas_ordem6)
############################

#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem7 = []
for musica in lista_album_imunidade:
   nome_musica7 = musica.text
   musicas_ordem7.append(nome_musica7)
print(musicas_ordem7)
###########################

#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem8 = []
for musica in lista_album_ritmo:
   nome_musica8 = musica.text
   musicas_ordem8.append(nome_musica8)
print(musicas_ordem8)
################################

#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem9 = []
for musica in lista_album_camisa:
   nome_musica9 = musica.text
   musicas_ordem9.append(nome_musica9)
print(musicas_ordem9)

#########################
#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem10 = []
for musica in lista_album_la:
   nome_musica10 = musica.text
   musicas_ordem10.append(nome_musica10)
print(musicas_ordem10)

#------------------------------

musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
print(musicas_ordem)

###########################
musicas_ordem2 = [item.replace("\xa0", "") for item in musicas_ordem2]
musicas_ordem2 = [item.replace("\n", "") for item in musicas_ordem2]
musicas_ordem2 = [item.replace('"', "") for item in musicas_ordem2]
print(musicas_ordem2)

#############################

musicas_ordem3 = [item.replace("\xa0", "") for item in musicas_ordem3]
musicas_ordem3 = [item.replace("\n", "") for item in musicas_ordem3]
musicas_ordem3 = [item.replace('"', "") for item in musicas_ordem3]
print(musicas_ordem3)

#################################
musicas_ordem4 = [item.replace("\xa0", "") for item in musicas_ordem4]
musicas_ordem4 = [item.replace("\n", "") for item in musicas_ordem4]
musicas_ordem4 = [item.replace('"', "") for item in musicas_ordem4]
print(musicas_ordem4)
##############################

musicas_ordem5 = [item.replace("\xa0", "") for item in musicas_ordem5]
musicas_ordem5 = [item.replace("\n", "") for item in musicas_ordem5]
musicas_ordem5 = [item.replace('"', "") for item in musicas_ordem5]
print(musicas_ordem5)

##############################
musicas_ordem6 = [item.replace("\xa0", "") for item in musicas_ordem6]
musicas_ordem6 = [item.replace("\n", "") for item in musicas_ordem6]
musicas_ordem6 = [item.replace('"', "") for item in musicas_ordem6]
print(musicas_ordem6)
###############################
musicas_ordem7 = [item.replace("\xa0", "") for item in musicas_ordem7]
musicas_ordem7 = [item.replace("\n", "") for item in musicas_ordem7]
musicas_ordem7 = [item.replace('"', "") for item in musicas_ordem7]
print(musicas_ordem7)
#################################

musicas_ordem8 = [item.replace("\xa0", "") for item in musicas_ordem8]
musicas_ordem8 = [item.replace("\n", "") for item in musicas_ordem8]
musicas_ordem8 = [item.replace('"', "") for item in musicas_ordem8]
print(musicas_ordem8)
###############################

musicas_ordem9 = [item.replace("\xa0", "") for item in musicas_ordem9]
musicas_ordem9 = [item.replace("\n", "") for item in musicas_ordem9]
musicas_ordem9 = [item.replace('"', "") for item in musicas_ordem9]
print(musicas_ordem9)

#######################

musicas_ordem10 = [item.replace("\xa0", "") for item in musicas_ordem10]
musicas_ordem10 = [item.replace("\n", "") for item in musicas_ordem10]
musicas_ordem10 = [item.replace('"', "") for item in musicas_ordem10]
print(musicas_ordem10)

#-------------------------------------

#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_transp = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_transp)

###############################
#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_curto = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_curto)

##################################

#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_nadando = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_nadando)

##########################################

#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_abalando = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_abalando)
######################################

#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_bocas = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_bocas)

######################################
#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_tamo = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_tamo)
#####################################
#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_imunidade = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_imunidade)
##################################

#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_ritmo = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_ritmo)
######################################

#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_camisa = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_camisa)

#######################################

#Buscando a minutagem das músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_la = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})
#Conferindo o se o número de músicas encontradas condiz com o esperado
print(lista_album_la)


#----------------------------------
musicas_ordem = []
for musica in lista_album_transp:
   nome_musica = musica.text
   musicas_ordem.append(nome_musica)
print(musicas_ordem)

#############################
musicas_ordem2 = []
for musica in lista_album_curto:
   nome_musica2 = musica.text
   musicas_ordem2.append(nome_musica2)
print(musicas_ordem2)

#############################

musicas_ordem3 = []
for musica in lista_album_nadando:
   nome_musica3 = musica.text
   musicas_ordem3.append(nome_musica3)
print(musicas_ordem3)

###########################

musicas_ordem4 = []
for musica in lista_album_abalando:
   nome_musica4 = musica.text
   musicas_ordem4.append(nome_musica4)
print(musicas_ordem4)

###########################

musicas_ordem5 = []
for musica in lista_album_bocas:
   nome_musica5 = musica.text
   musicas_ordem5.append(nome_musica5)
print(musicas_ordem5)

################################

musicas_ordem6 = []
for musica in lista_album_tamo:
   nome_musica6 = musica.text
   musicas_ordem6.append(nome_musica6)
print(musicas_ordem6)
############################
musicas_ordem7 = []
for musica in lista_album_imunidade:
   nome_musica7 = musica.text
   musicas_ordem7.append(nome_musica7)
print(musicas_ordem7)
##############################

musicas_ordem8 = []
for musica in lista_album_ritmo:
   nome_musica8 = musica.text
   musicas_ordem8.append(nome_musica8)
print(musicas_ordem8)

#################################

musicas_ordem9 = []
for musica in lista_album_camisa:
   nome_musica9 = musica.text
   musicas_ordem9.append(nome_musica9)
print(musicas_ordem9)

#######################################

musicas_ordem10 = []
for musica in lista_album_la:
   nome_musica10 = musica.text
   musicas_ordem10.append(nome_musica10)
print(musicas_ordem10)

