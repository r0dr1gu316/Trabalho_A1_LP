import pandas as pd
from coleta_manual import ordem_albunsdf
from coleta_manual import data_lanc_albuns
from IPython.display import display 

df_albuns = pd.DataFrame({'Lançamento':data_lanc_albuns}, index=[ordem_albunsdf])
#display(df_albuns)
