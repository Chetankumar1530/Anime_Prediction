import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = pd.read_csv("anime.csv")
data.genre.fillna(" ",inplace=True)

tfid = TfidfVectorizer(stop_words="english")
vector = tfid.fit_transform(data.genre)
index =pd.Series(data = data.index, index=data.name)


def anime_hunt(name,n =10):

    ind_name = index[name]
    dis = linear_kernel(vector[ind_name],vector)
    val_name = list((dis))
    d = pd.DataFrame(val_name )
    
    d = d.transpose()
    d.columns = ["name"]
    d = d.sort_values(by="name" ,ascending=False)
    l=[]

    for i in range (0,10):
        l.append(data.name.loc[d.index[i]])
    return l

# def anime_pred(name,n):   
#     ind_name = index[name]
#     val_name = list(enumerate(dis[ind_name]))
#     val_name =sorted(val_name,key=lambda x : x[1] ,reverse=True)
#     l = []
#     for i in range (0,n):
#         l.append(data.name.loc[val_name[i][0]])
#     return l

def genere(name,n):   
    ind_name = index[name]
    dis = linear_kernel(vector[ind_name],vector)
    val_name = list((dis))
    d = pd.DataFrame(val_name )
    
    d = d.transpose()
    d.columns = ["name"]
    d = d.sort_values(by="name" ,ascending=False)
    l=[]

    for i in range (0,10):
        l.append(data.genre.loc[d.index[i]])
    return l

def rating(name,n):   
    ind_name = index[name]
    dis = linear_kernel(vector[ind_name],vector)
    val_name = list((dis))
    d = pd.DataFrame(val_name )
    
    d = d.transpose()
    d.columns = ["name"]
    d = d.sort_values(by="name" ,ascending=False)
    l=[]

    for i in range (0,10):
        l.append(data.rating.loc[d.index[i]])
    return l


def checker(name):
    if name in index:
        return ["hi","hi","hi", "hi","hi"]
    else:
        return ["hi","hi"]


def list_name():
    return data.name

def list_gene():
    return data.genre

def list_rating():
    return data.rating