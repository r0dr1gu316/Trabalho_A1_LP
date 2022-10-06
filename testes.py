import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re

def pegar_info_nome(link):
    pag = requests.get(link)
    html_bruto = pag.text
    html_arrumado = BeautifulSoup(html_bruto, 'html.parser')
    lista_album_transp = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})
    musicas_ordem = []
    for musica in lista_album_transp:
        nome_musica = musica.text
        musicas_ordem.append(nome_musica)
    musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
    musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
    musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
    return musicas_ordem



def pegar_info_tempo(link):
    pag = requests.get(link)
    html_bruto = pag.text
    html_arrumado = BeautifulSoup(html_bruto, 'html.parser')
    lista_album_transp = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})
    musicas_ordem = []
    for musica in lista_album_transp:
        nome_musica = musica.text
        musicas_ordem.append(nome_musica)
    musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
    musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
    musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
    del musicas_ordem [::2]
    return musicas_ordem
    

##############################

musicas_transp = pegar_info_nome('https://pt.wikipedia.org/wiki/Transpira%C3%A7%C3%A3o_Cont%C3%ADnua_Prolongada')
del musicas_transp[16:]
print(musicas_transp)

tempos_transp = pegar_info_tempo('https://pt.wikipedia.org/wiki/Transpira%C3%A7%C3%A3o_Cont%C3%ADnua_Prolongada')
del tempos_transp [16:]
print(tempos_transp)

##############################

musicas_curto = pegar_info_nome('https://pt.wikipedia.org/wiki/Pre%C3%A7o_Curto..._Prazo_Longo')
print(musicas_curto)

tempos_curto = pegar_info_tempo('https://pt.wikipedia.org/wiki/Pre%C3%A7o_Curto..._Prazo_Longo')
print(tempos_curto)

##############################

musicas_nadando = pegar_info_nome('https://pt.wikipedia.org/wiki/Nadando_com_os_Tubar%C3%B5es')
print(musicas_nadando)

tempos_nadando = pegar_info_tempo('https://pt.wikipedia.org/wiki/Nadando_com_os_Tubar%C3%B5es')
print(tempos_nadando)

##############################

musicas_abalando = pegar_info_nome('https://pt.wikipedia.org/wiki/100%25_Charlie_Brown_Jr._-_Abalando_a_Sua_F%C3%A1brica')
print(musicas_abalando)

tempos_abalando = pegar_info_tempo('https://pt.wikipedia.org/wiki/100%25_Charlie_Brown_Jr._-_Abalando_a_Sua_F%C3%A1brica')
print(tempos_abalando)

##############################

musicas_bocas = pegar_info_nome('https://pt.wikipedia.org/wiki/Bocas_Ordin%C3%A1rias')
print(musicas_bocas)

tempos_bocas = pegar_info_tempo('https://pt.wikipedia.org/wiki/Bocas_Ordin%C3%A1rias')
print(tempos_bocas)

##############################

musicas_tamo = pegar_info_nome('https://pt.wikipedia.org/wiki/Tamo_A%C3%AD_na_Atividade')
print(musicas_tamo)

tempos_tamo = pegar_info_tempo('https://pt.wikipedia.org/wiki/Tamo_A%C3%AD_na_Atividade')
print(tempos_tamo)

##############################

musicas_imunidade = pegar_info_nome('https://pt.wikipedia.org/wiki/Imunidade_Musical')
print(musicas_imunidade)

tempos_imunidade = pegar_info_tempo('https://pt.wikipedia.org/wiki/Imunidade_Musical')
print(tempos_imunidade)


##############################

musicas_ritmo = pegar_info_nome('https://pt.wikipedia.org/wiki/Ritmo,_Ritual_e_Responsa')
print(musicas_ritmo)

tempos_ritmo = pegar_info_tempo('https://pt.wikipedia.org/wiki/Ritmo,_Ritual_e_Responsa')
print(tempos_ritmo)

##############################

musicas_camisa = pegar_info_nome('https://pt.wikipedia.org/wiki/Camisa_10_Joga_Bola_At%C3%A9_na_Chuva')
print(musicas_camisa)

tempos_camisa = pegar_info_tempo('https://pt.wikipedia.org/wiki/Camisa_10_Joga_Bola_At%C3%A9_na_Chuva')
print(tempos_camisa)

################################

musicas_la = pegar_info_nome('https://pt.wikipedia.org/wiki/La_Familia_013')
print(musicas_la)

tempos_la = pegar_info_tempo('https://pt.wikipedia.org/wiki/La_Familia_013')
print(tempos_la)
