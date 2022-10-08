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

    
#pode dar ruim no final pois a lista ja deveria estar definida antes e nao somente aqui
#adicionando nome split de cada musica em uma lista
nome_das_musicas = list()
for a in range(0, len(nome_das_musicas)):
    espacar =  nome_das_musicas[a].count(' ')
    palavra = nome_das_musicas[a].lower()
    for a in range(0, espacar):
        pos = palavra.find(' ')
        adicionar = palavra[0:pos]
        add = str(adicionar)
        add = add.replace("'",'')
        add = add.replace('(','')
        add = add.replace(')','')
        add = add.replace('.','')
        add = add.replace('/','')
        nome_das_musicas_split.append(add)
        palavra = palavra[pos+1:]
        
    nome_das_musicas_split.append(palavra)

#adicionando nome split de cada album em uma lista
nome_dos_discos = list()
for a in range(0, len(nome_dos_discos)):
    espacar = nome_dos_discos[a].count(' ')
    palavra = nome_dos_discos[a].lower()
    for a in range(0, space):
        pos = palavra.find(' ')
        adivionar = palavra[0:pos]
        add = str(adicionar)
        add = add.replace("'",'')
        add = add.replace('(','')
        add = add.replace(')','')
        add = add.replace('.','')
        add = add.replace('/','')
        nome_dos_discos_split.append(add)
        palavra = palavra[pos+1:]
        
    nome_dos_discos_split.append(palavra)

link_das_musicas = list()
link_padrao = 'https://www.vagalume.com.br/'
for word in html_arrumado.find_all('div', class_ = 'lineColLeft'):
    secao = str(word)
    if 'href="' in secao:
        pos = secao.find('href="')
        add = secao[pos+6:]
        pos2 = add.find('""')
        add = add[:pos2]
        add = link_padrao + add
        link_das_musicas.append(add)
        
#ajustando o dicionario
nome_dos_discos = list()
lirics = list()
for a in range(0, len(nome_dos_discos)):
    dicionario[nome_dos_discos[a]] = dict()
    
    words = nome_dos_discos[0].count(' ')+1
    dicionario[nome_dos_discos[a]]['Nome Album Split:']=  nome_dos_discos_split[0:words]
    del nome_dos_discos_split[0:words]
    
    lista_nomes_falsa = list()
    lista_nomes_falsa = nome_das_musicas[:quantidade_musicas[a]]
    del nome_das_musicas[:quantidade_musicas[a]]
    
    dicionario[nome_dos_discos[a]]['musicas:'] =  lista_nomes_falsa
    
    nome_das_musicas_split = list()
    lista_nomes_falsa = list()
    for b in range(0, len(lista_nomes_falsa)):
        espacar = lista_nomes_falsa[b].count(' ')
        palavra = lista_nomes_falsa[b].lower()
        for c in range(0, espacar+1):
            pos = palavra.find(' ')
            if pos == -1:
                add = str(palavra)
            else:
                add = str(palavra[0:pos])
            
            add = add.replace("'",'')
            add = add.replace('(','')
            add = add.replace(')','')
            add = add.replace('.','')
            add = add.replace('/','')
            nome_das_musicas_split.append(add)
            palavra = palavra[pos+1:]
    
        dicionario[nome_dos_discos[a]]['Nome Musicas Split:'] = nome_das_musicas_split
        dicionario[nome_dos_discos[a]]['Quantidade de  Musicas:'] = quantidade_musicas[a]
    
        links = list()
        links = link_das_musicas[0:mus]
        del link_das_musicas[0:mus]
    
        dicionario[nome_dos_discos[a]]['Links das Musicas:'] = links
    
        for d in range(0, len(links)):
            pag = requests.get(links[d])
            html_final = BeautifulSoup(pag.text, 'lxml')
            letra = html_final.find_all('div', id='lyrics')
            
            letra = str(letra[0])
            
            x = letra.find('>')
            letra = letra[x+1:]
            
            partes = letra.count('>')
            
            lirics = ''
            
            for a in range(0, partes):
                x = letra.find('<')
                
                lirics += letra[0:x]
                if x != 0:
                    lirics += ' '
                
                y = letra.find('>')
                letra = letra[y+1:]
                
print(lirics)     
print(dicionario)  
    
