import numpy as np
import pandas as pd
ndata = np.array(['jus',10,20,True])
# print(ndata,type(ndata))
ps=pd.Series(ndata)
print(ps,type(ps))