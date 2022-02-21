import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv("anime.csv")
data.genre.fillna(" ",inplace=True)

tfid = TfidfVectorizer(stop_words="english")
vector = tfid.fit_transform(data.genre)
dis = linear_kernel(vector,vector)
index =pd.Series(data = data.index, index=data.name)
def anime_pred(name,n):   
    ind_name = index[name]
    val_name = list(enumerate(dis[ind_name]))
    val_name =sorted(val_name,key=lambda x : x[1] ,reverse=True)
    l = []
    for i in range (0,n):
        l.append(data.name.loc[val_name[i][0]])
    return l

def genere(name,n):   
    ind_name = index[name]
    val_name = list(enumerate(dis[ind_name]))
    val_name =sorted(val_name,key=lambda x : x[1] ,reverse=True)
    l = []
    for i in range (0,n):
        l.append(data.genre.loc[val_name[i][0]])
    return l

def rating(name,n):   
    ind_name = index[name]
    val_name = list(enumerate(dis[ind_name]))
    val_name =sorted(val_name,key=lambda x : x[1] ,reverse=True)
    l = []
    for i in range (0,n):
        l.append(data.rating.loc[val_name[i][0]])
    return l


def checker(name):
    if name in index:
        return ["hi","hi","hi", "hi","hi"]
    else:
        return ["hi","hi"]
