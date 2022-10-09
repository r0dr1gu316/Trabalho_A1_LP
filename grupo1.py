import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
from functools import reduce
from spotipy.oauth2 import SpotifyClientCredentials
from IPython.display import display 
from coleta_manual import ordem_albunsdf
from coleta_manual import premios_albumdf
from coleta_manual import categorias_premio
from coleta_manual import certificacoes_albuns
from coleta_manual import data_lanc_albuns

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

# Processo para coleta de dados da popularidade das músicas no spotify:
cid = '4c3f7f276b104969844fda46b330e711'
secret = '7ada4d46d6e1409b9424c359c03e28cb'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = cid, client_secret = secret))

# link de cada álbum
link_transpiracao = '09Nao8wNpzTz60nY8G2n7A'
link_preco = '2hLNxoJZ5kZoBEX0XGBRNu'
link_tubaroes = '5eF1HzO5mIQxs7bCwW9TJC'
link_Cbjr = '0Dcy3ThOh8LS1qhXUbZWH7'
link_bocas = '1FsdTRaD7Ec15uKh71PhkE'
link_acustico = '0AFkktyrrPtQvpIBqpRrc7'
link_tamoai = '6PsijYuoyIB4vgV5brmbhq'
link_imunidade = '1l8K5fgYz4J0ZZyjMVd6Q1'
link_RRR = '0wHl2FK2AEhwIiYISv7cJ4'
link_camisa10 = '0tbiBipiOorOAnL7XWFbgt'
link_MPC = '4j8gmVMG1HM5oNyKRYNJWB'
link_013 = '53GOG940xY4LOpgD8YzQrJ'


 
# Função para coletar as musicas mais populares da história da banda
def popularidade_banda(spotify_id_list: list):
    lista_popularidade_banda = []

    for spotify_id in spotify_id_list:
        lista_popularidade_banda += musicas_populares_album(spotify_id)
        dados = {'Popularidade': lista_popularidade_banda}
        df = pd.DataFrame(data=dados)
    return df

#----Pergunta 1 Item i----#

# Função para coletar as musicas mais populares de cada álbum:
def musicas_populares_album(spotify_id: str):
    results = spotify.album_tracks(spotify_id)
    tracks = results['items']
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results)

    lista_popularidade = []

    for track in tracks:
        track_id = track['id']
        track_page = spotify.track(track_id)
        popularity = track_page['popularity']
        lista_popularidade.append(popularity)
    return lista_popularidade

#print('Transpiração Contínua:',musicas_populares_album(link_transpiracao))

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

#----Pergunta 1 Item iii----#
# Função para coletar as musicas mais populares da história da banda
def popularidade_banda(spotify_id_list: list):
    lista_popularidade_banda = []

    for spotify_id in spotify_id_list:
        lista_popularidade_banda += musicas_populares_album(spotify_id)
        dados = {'Popularidade': lista_popularidade_banda}
        df = pd.DataFrame(data=dados)
    return df

df_musicas = popularidade_banda([link_transpiracao, link_preco, link_tubaroes, link_Cbjr, link_bocas, link_acustico, link_tamoai, link_imunidade, link_RRR, link_camisa10, link_MPC, link_013])
#print(df_musicas)

dfs = pd.concat([df_duracao_transpiracao, df_duracao_preco, df_duracao_nadando, df_duracao_abalando, df_duracao_bocas, df_duracao_tamoai,
df_duracao_imunidade, df_duracao_ritmo, df_duracao_camisa, df_duracao_013, df_duracao_charlie, df_duracao_caicara],
keys=['Transpiração Contínua Prolongada', 'Preço Curto... Prazo Longo', 'Nadando com os Tubarões', '100% Charlie Brown Jr. - Abalando a Sua Fábrica', 'Bocas Ordinárias',
'Tamo Aí na Atividade', 'Imunidade Musical','Ritmo, Ritual e Responsa','Camisa 10 Joga Bola Até na Chuva','La Familia 013','Acústico MTV: Charlie Brown Jr.',
'Música Popular Caiçara ao Vivo'])
print(dfs)

#Removendo linhas que estavam a mais no DataFrame para a concatenação:
dfs = dfs.drop(dfs.index[[43, 45, 53, 126, 150, 153]])

#Exportando para csv
dfs.to_csv('Músicas_CBJR')
## Há 2 colunas com Numero de Faixas e Nome dos álbuns que
#pd.set_option('display.max_columns', 200)
#pd.set_option('display.max_rows', 200)
df_total = pd.read_csv('Músicas_CBJR')
print(df_total)

#df_completo = pd.concat([dfs, df_musicas], axis = 1)
print(df_completo)

# Concatenando o DataFrame de popularidade com o DataFrame total:
df_completo = pd.concat([df_total, df_musicas], axis = 1)
#pd.set_option('display.max_columns', 200)
#pd.set_option('display.max_rows', 200)
print(df_completo)

## Exibindo o top 3 de músicas mais ouvidas e menos ouvidas na historia da banda, atraves da popularidade
def popularidade(exibicao):
    mais_populares = exibicao.nlargest(3, columns = 'Popularidade')
    menos_populares = exibicao.nsmallest(3, columns = 'Popularidade')
    return print('Mais Populares:', '\n', mais_populares, '\n\n', 'Menos Populares:', menos_populares)

## Exibição de colunas e linhas totais no dataframe
#pd.set_option('display.max_columns', 200)
#pd.set_option('display.max_rows', 200)
print(popularidade(df_completo))

#----Pergunta 1 Item iv----#
#Unindo os DataFrames para que seja possivel pegar o Top 3 de toda  historia a banda
dfs1 = [df_duracao_transpiracao, df_duracao_preco, df_duracao_nadando, df_duracao_abalando, df_duracao_bocas, df_duracao_tamoai,
df_duracao_imunidade, df_duracao_ritmo, df_duracao_camisa, df_duracao_013, df_duracao_charlie, df_duracao_basica] # list of dataframes
df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Nome da Música', 'Duração da Música'],
                                            how='outer'), dfs1)
print(minutagem(df_merged))

#----Pergunta 1 Item v----#
#Adicionando ao DataFrame as premiações das músicas através da lista criada em (coleta_premios)
df_albuns = pd.DataFrame({'Premio':premios_albumdf, 'Categoria':categorias_premio, 'Certificações':certificacoes_albuns}, index=[ordem_albunsdf])
#display(df_albuns)


#----Pergunta 1 Item vi----#
#Através da análise do dataframe completo podemos perceber que as músicas que possuem a maior popularidade, ou seja, as mais ouvidas, relacionadas com a duração da música não possuem duração. 

dfs.to_csv('Músicas_CBJR')
df_total = pd.read_csv('Músicas_CBJR')
print(df_total)

#df_completo = pd.concat([dfs, df_musicas], axis = 1)
#print(df_completo)

df_completo = pd.concat([df_total, df_musicas], axis = 1)
#pd.set_option('display.max_columns', 200)
#pd.set_option('display.max_rows', 200)
print(df_completo)

def popularidade(exibicao):
    mais_populares = exibicao.nlargest(3, columns = 'Popularidade')
    menos_populares = exibicao.nsmallest(3, columns = 'Popularidade')
    return print('Mais Populares:', '\n', mais_populares, '\n\n', 'Menos Populares:', menos_populares)

#pd.set_option('display.max_columns', 200)
#pd.set_option('display.max_rows', 200)
print(popularidade(df_completo))
