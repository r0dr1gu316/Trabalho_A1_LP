from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import unidecode

quantidade_musicas = list()
nome_das_musicas_split = list()
nome_dos_discos_split = list()

dicionario = dict()

html_bruto = requests.get('https://www.vagalume.com.br/charlie-brown-jr/discografia/')
html_arrumado = BeautifulSoup(html_bruto.text, 'html.parser')

#nome das musicas
nome_das_musicas = list()
for word in html_arrumado.find_all('a'):
    if 'nameMusic' in str(word):
        nome_das_musicas.append(word.get_text())


#pegando nome dos albúns
nome_dos_discos = list()
for word in html_arrumado.find_all('h3'):
    if 'albumTitle' in str(word):
        nome_dos_discos.append(word.get_text())

#print(nome_dos_discos)



#pegando a quantidade de músicas em cada álbum
for word in html_arrumado.find_all('div', class_='trackWrapper'):
    musicas_por_album = word.get_text()
    f = musicas_por_album.find('f')
    musicas_por_album = musicas_por_album[2:f-1]
    musicas_por_album = int(musicas_por_album)
    nome_das_musicas.append(musicas_por_album)
