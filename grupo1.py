import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
from functools import reduce
from IPython.display import display 

#Função responsavel por buscar o nome das musicas no site
def pegar_info_nome(link):
    pag = requests.get(link)
    html_bruto = pag.text
    html_arrumado = BeautifulSoup(html_bruto, 'html.parser')
    lista_album_transpiracao = html_arrumado.find_all('td', {'style': 'text-align: left; vertical-align: top;'})
    musicas_ordem = []
    for musica in lista_album_transpiracao:
        nome_musica = musica.text
        musicas_ordem.append(nome_musica)
    musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
    musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
    musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
    return musicas_ordem

#Função responsavel por buscar a minutagem das musicas no site
def pegar_info_tempo(link):
    pag = requests.get(link)
    html_bruto = pag.text
    html_arrumado = BeautifulSoup(html_bruto, 'html.parser')
    lista_album_transpiracao = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; vertical-align: top;'})
    musicas_ordem = []
    for musica in lista_album_transpiracao:
        nome_musica = musica.text
        musicas_ordem.append(nome_musica)
    musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
    musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
    musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
    del musicas_ordem[::2]
    return musicas_ordem

#Criando variaveis para o site de cada album e fazendo a limpeza dos dados

musicas_transpiracao = pegar_info_nome('https://pt.wikipedia.org/wiki/Transpira%C3%A7%C3%A3o_Cont%C3%ADnua_Prolongada')
del musicas_transpiracao[16:]
#print(musicas_transpiracao)
tempos_transpiracao = pegar_info_tempo('https://pt.wikipedia.org/wiki/Transpira%C3%A7%C3%A3o_Cont%C3%ADnua_Prolongada')
del tempos_transpiracao[16:]
#print(tempos_transpiracao)

musicas_preco = pegar_info_nome('https://pt.wikipedia.org/wiki/Pre%C3%A7o_Curto..._Prazo_Longo')
#print(musicas_preco)
tempos_preco = pegar_info_tempo('https://pt.wikipedia.org/wiki/Pre%C3%A7o_Curto..._Prazo_Longo')
#print(tempos_preco)

musicas_nadando = pegar_info_nome('https://pt.wikipedia.org/wiki/Nadando_com_os_Tubar%C3%B5es')
#print(musicas_nadando)
tempos_nadando = pegar_info_tempo('https://pt.wikipedia.org/wiki/Nadando_com_os_Tubar%C3%B5es')
#print(tempos_nadando)

musicas_abalando = pegar_info_nome('https://pt.wikipedia.org/wiki/100%25_Charlie_Brown_Jr._-_Abalando_a_Sua_F%C3%A1brica')
#print(musicas_abalando)
tempos_abalando = pegar_info_tempo('https://pt.wikipedia.org/wiki/100%25_Charlie_Brown_Jr._-_Abalando_a_Sua_F%C3%A1brica')
#print(tempos_abalando)

musicas_bocas = pegar_info_nome('https://pt.wikipedia.org/wiki/Bocas_Ordin%C3%A1rias')
#print(musicas_bocas)
tempos_bocas = pegar_info_tempo('https://pt.wikipedia.org/wiki/Bocas_Ordin%C3%A1rias')
#print(tempos_bocas)

musicas_tamoai = pegar_info_nome('https://pt.wikipedia.org/wiki/Tamo_A%C3%AD_na_Atividade')
#print(musicas_tamoai)
tempos_tamoai = pegar_info_tempo('https://pt.wikipedia.org/wiki/Tamo_A%C3%AD_na_Atividade')
#print(tempos_tamoai)

musicas_imunidade = pegar_info_nome('https://pt.wikipedia.org/wiki/Imunidade_Musical')
#print(musicas_imunidade)
tempos_imunidade = pegar_info_tempo('https://pt.wikipedia.org/wiki/Imunidade_Musical')
#print(tempos_imunidade)

musicas_ritmo = pegar_info_nome('https://pt.wikipedia.org/wiki/Ritmo,_Ritual_e_Responsa')
#print(musicas_ritmo)
tempos_ritmo = pegar_info_tempo('https://pt.wikipedia.org/wiki/Ritmo,_Ritual_e_Responsa')
#print(tempos_ritmo)

musicas_camisa = pegar_info_nome('https://pt.wikipedia.org/wiki/Camisa_10_Joga_Bola_At%C3%A9_na_Chuva')
#print(musicas_camisa)
tempos_camisa = pegar_info_tempo('https://pt.wikipedia.org/wiki/Camisa_10_Joga_Bola_At%C3%A9_na_Chuva')
#limpando os dados
tempos_camisa_novo = []
for string in tempos_camisa:
    a = string[1:]
    tempos_camisa_novo.append(a)
#print(tempos_camisa_novo)

musicas_013 = pegar_info_nome('https://pt.wikipedia.org/wiki/La_Familia_013')
#print(musicas_013)
tempos_013 = pegar_info_tempo('https://pt.wikipedia.org/wiki/La_Familia_013')
#print(tempos_013)

musicas_charlie = pegar_info_nome('https://pt.wikipedia.org/wiki/Ac%C3%BAstico_MTV:_Charlie_Brown_Jr.')
#print(musicas_charlie)
tempos_charlie = pegar_info_tempo('https://pt.wikipedia.org/wiki/Ac%C3%BAstico_MTV:_Charlie_Brown_Jr.')
#print(tempos_charlie)

musicas_basica = pegar_info_nome('https://pt.wikipedia.org/wiki/M%C3%BAsica_Popular_Cai%C3%A7ara_ao_Vivo')
del musicas_basica[16:]
#print(musicas_basica)
tempos_basica = pegar_info_tempo('https://pt.wikipedia.org/wiki/M%C3%BAsica_Popular_Cai%C3%A7ara_ao_Vivo')
#print(tempos_basica)

#------------------------------------------------------------

#Fazendo o DataFrame de cada album para pegarmos as musicas mais longas e mais curtas 
df_duracao_transpiracao = pd.DataFrame(zip(musicas_transpiracao, tempos_transpiracao), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_preco = pd.DataFrame(zip(musicas_preco, tempos_preco), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_nadando = pd.DataFrame(zip(musicas_nadando, tempos_nadando), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_abalando = pd.DataFrame(zip(musicas_abalando, tempos_abalando), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_bocas= pd.DataFrame(zip(musicas_bocas, tempos_bocas), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_tamoai = pd.DataFrame(zip(musicas_tamoai, tempos_tamoai), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_imunidade = pd.DataFrame(zip(musicas_imunidade, tempos_imunidade), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_ritmo = pd.DataFrame(zip(musicas_ritmo, tempos_ritmo), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_camisa = pd.DataFrame(zip(musicas_camisa, tempos_camisa_novo), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_013 = pd.DataFrame(zip(musicas_013, tempos_013), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_charlie = pd.DataFrame(zip(musicas_charlie, tempos_charlie), columns = ['Nome da Música', 'Duração da Música'])

df_duracao_basica = pd.DataFrame(zip(musicas_basica, tempos_basica), columns = ['Nome da Música', 'Duração da Música'])

#----Pergunta 1 Item ii----#
#função responsavel por listar todas as musicas em ordem de minutagem e pegar o top 3 musicas mais longas e mais curtas
def minutagem(tempo):
    mais_duradouras = tempo.sort_values(by = 'Duração da Música', ascending = False)
    menos_duradouras = tempo.sort_values(by = 'Duração da Música', ascending = True)
    
    top_mais_duradouras = mais_duradouras[:3]
    top_menos_duradouras = menos_duradouras[:3]
    return print('Mais longas:','\n',top_mais_duradouras,'\n\n', 'Mais Curtas:', top_menos_duradouras)

#resultado do top 3 mais longas e mais curtas de cada album
print(minutagem(df_duracao_transpiracao), '#'*50, '\n')

print(minutagem(df_duracao_preco), '#'*50, '\n')

print(minutagem(df_duracao_nadando), '#'*50, '\n')

print(minutagem(df_duracao_abalando), '#'*50, '\n')

print(minutagem(df_duracao_bocas), '#'*50, '\n')

print(minutagem(df_duracao_tamoai), '#'*50, '\n')

print(minutagem(df_duracao_imunidade), '#'*50, '\n')

print(minutagem(df_duracao_ritmo), '#'*50, '\n')

print(minutagem(df_duracao_camisa), '#'*50, '\n')

print(minutagem(df_duracao_013), '#'*50, '\n')

print(minutagem(df_duracao_charlie), '#'*50, '\n')

print(minutagem(df_duracao_basica), '#'*50, '\n')

#----Pergunta 1 Item iv----#
#Unindo os DataFrames para que seja possivel pegar o Top 3 de todo a historiada banda
dfs = [df_duracao_transpiracao, df_duracao_preco, df_duracao_nadando, df_duracao_abalando, df_duracao_bocas, df_duracao_tamoai,
df_duracao_imunidade, df_duracao_ritmo, df_duracao_camisa, df_duracao_013, df_duracao_charlie, df_duracao_basica] # list of dataframes
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Nome da Música', 'Duração da Música'],
                                            how='outer'), dfs)

print(minutagem(df_merged))
