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

#Buscando as músicas na estrutura html através de seus atributos que foram encontrados por meio da funcionalidade inspecionar do navegador 
lista_album_transp = html_arrumado.find_all('td',{'style':'text-align: left; vertical-align: top;'})

#Obtendo a variável que ordena as músicas por mais ouvida para utilizar futuramente no código
musicas_ordem = []
for musica in lista_album_transp:
   nome_musica = musica.text
   musicas_ordem.append(nome_musica)
#print(musicas_ordem)

musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
print(musicas_ordem)

lista_album_transp = html_arrumado.find_all('td',{'style':'padding-right: 10px; text-align: right; vertical-align: top;'})


musicas_ordem = []
for musica in lista_album_transp:
   nome_musica = musica.text
   musicas_ordem.append(nome_musica)
#print(musicas_ordem)

musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
print(musicas_ordem)

















