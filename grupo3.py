import pandas as pd
from coleta_manual import ordem_albunsdf
from coleta_manual import data_lanc_albuns
from IPython.display import display 


#Grupo 3 Pergunta 1- Qual a data de lançamento de cada album?
df_albuns = pd.DataFrame({'Lançamento':data_lanc_albuns}, index=[ordem_albunsdf])
display(df_albuns)


#Grupo 3 Pergunta 2- Qual a minutagem total de cada album?
def tempo_album(link):
    pag = requests.get(link)
    html_bruto = pag.text
    html_arrumado = BeautifulSoup(html_bruto, 'html.parser')
    lista_album_transpiracao = html_arrumado.find_all('td', {'style': 'padding-right: 10px; text-align: right; background-color: #eee;'})
    musicas_ordem = []
    for musica in lista_album_transpiracao:
        nome_musica = musica.text
        musicas_ordem.append(nome_musica)
    musicas_ordem = [item.replace("\xa0", "") for item in musicas_ordem]
    musicas_ordem = [item.replace("\n", "") for item in musicas_ordem]
    musicas_ordem = [item.replace('"', "") for item in musicas_ordem]
    return musicas_ordem
  
 album_transpiracao = tempo_album('https://pt.wikipedia.org/wiki/Transpira%C3%A7%C3%A3o_Cont%C3%ADnua_Prolongada')
print(album_transpiracao)

album_preco = tempo_album('https://pt.wikipedia.org/wiki/Pre%C3%A7o_Curto..._Prazo_Longo')
print(album_preco)

album_nadando = tempo_album('https://pt.wikipedia.org/wiki/Nadando_com_os_Tubar%C3%B5es')
print(album_nadando)

album_abalando = tempo_album('https://pt.wikipedia.org/wiki/100%25_Charlie_Brown_Jr._-_Abalando_a_Sua_F%C3%A1brica')
print(album_abalando)

album_bocas =  tempo_album('https://pt.wikipedia.org/wiki/Bocas_Ordin%C3%A1rias')
album_bocas = ['42:25']
print(album_bocas)

album_tamoai =  tempo_album('https://pt.wikipedia.org/wiki/Tamo_A%C3%AD_na_Atividade')
album_tamoai = ['42:16']
print(album_tamoai)

album_imunidade =  tempo_album('https://pt.wikipedia.org/wiki/Imunidade_Musical')
print(album_imunidade)

album_ritmo =  tempo_album('https://pt.wikipedia.org/wiki/Ritmo,_Ritual_e_Responsa')
print(album_ritmo)

album_camisa =  tempo_album('https://pt.wikipedia.org/wiki/Camisa_10_Joga_Bola_At%C3%A9_na_Chuva')
print(album_camisa)

album_013 =  tempo_album('https://pt.wikipedia.org/wiki/La_Familia_013')
print(album_013)

album_charlie =  tempo_album('https://pt.wikipedia.org/wiki/Ac%C3%BAstico_MTV:_Charlie_Brown_Jr.')
print(album_charlie)

album_basica =  tempo_album('https://pt.wikipedia.org/wiki/M%C3%BAsica_Popular_Cai%C3%A7ara_ao_Vivo')
album_basica = ['47:25']
print(album_basica)

#Grupo 3 Pergunta 3- Qual Abum mais longo e o mais curto

