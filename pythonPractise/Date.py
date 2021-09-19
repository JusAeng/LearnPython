import datetime

def alpha():
    mill=datetime.date(2000,1,1)
    print(type(mill),mill)
    dt=datetime.timedelta(100)
    print(type(dt),"==",dt)
    print(mill+dt)


def beta():
    gvr = datetime.date(1956,1,31)
    #default: yyyy-mm-dd
    print(gvr)
    # print(gvr.day,gvr.month,gvr.year)
