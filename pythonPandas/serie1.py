import pandas as pd
import numpy as np

def besicSeries():
    data_ls = [10,20,'jus',14.12,'eiei'] #List
    data_tp = (10,20,'jus',14.12,'eiei') #tuple
    print(pd.Series(data_ls))
    print(pd.Series(data_tp))

def withNumpy():
    ndata = np.array(['jus',10,20,True])
    # print(ndata,type(ndata))
    ps=pd.Series(ndata)
    print(ps,type(ps))

def setIndex():
    items = ["mango","apple","banana"]
    idx = [50,20,30]
    print(pd.Series(items,index=idx))
def withDic():                                     #access Series
    fruit={"mango":50,"apple":20,"banana":30}
    a=pd.Series(fruit)
    print(a)
    print(a["apple"],a[0])
withDic()
