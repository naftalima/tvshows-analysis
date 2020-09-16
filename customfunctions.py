import pandas as pd
import numpy as np
import re

def functionnetworks_more_titlename(df_tt, networks): 
    column_names = list(df_tt.columns)
    df_most_popular = pd.DataFrame(columns = column_names)
    for i in networks:
        df = df_tt[df_tt['network'].str.contains(i, flags=re.IGNORECASE, regex=True, na=False)]
        df_most_popular = df_most_popular.append(df,ignore_index=True)
    return df_most_popular

# df_tvtime_amazon['name'].describe() # NÃO TA DUPLICADO