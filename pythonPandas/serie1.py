import pandas as pd
data_ls = [10,20,'jus',14.12,'eiei'] #List
data_tp = (10,20,'jus',14.12,'eiei') #tuple
print(pd.Series(data_ls))
print(pd.Series(data_tp))
