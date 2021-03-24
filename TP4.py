import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Fournie 
dic_abv = {'V': "victoire",
           'D': "defaite",
           'DP': "defaite par prolongation",
           'PTS': "points",
           'BP': "buts marquer",
           'BC': "buts encaisser",
           'DIFF': "difference de buts"}

division = ["Atlantic","Metropolitan","Central","Pacific"];

def lire_classement():
    classement = {}
    path = './classement2019.txt'

    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) > 1:
                line_splitted = line.split()
                # On sait que c'est une nouvelle division
                if line_splitted[0].isnumeric():
                    division = line_splitted[1]
                    classement[division] = {}
                else:
                    classement[division][line_splitted[0]] = {'ABV': line_splitted[1],
                                                              'MJ': int(line_splitted[2]),
                                                              'V': int(line_splitted[3]),
                                                              'D': int(line_splitted[4]),
                                                              'DP': int(line_splitted[5]),
                                                              'PTS': int(line_splitted[6]),
                                                              'VRP': int(line_splitted[7]),
                                                              'BP': int(line_splitted[8]),
                                                              'BC': int(line_splitted[9]),
                                                              'DIFF': int(line_splitted[10]),
                                                              'DIV': division}
    return classement

ligue_classement = lire_classement()


def creer_df(...):
    # To-Do: Vous devez creer votre dataframe a partir d'un dictionnaire
    # To-Do: Pour cela commencer par regrouper toute les equipe dans un seul dictionnaire
    # To-Do: Que vous allez convertir en dataframe. la fonction retourne un dataframe
    # Lien utile: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html

    
    return ...


def df_extraite_divison(...):
    # To-Do: la fonction retourne le dataframe de la division recu en parametre
    # To-Do: Vous devez enlever la column DIV de votre dataframe
    # Lien utile: https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html
    # Lien utile: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html
    return ...




def df_sort_type(...):
    #To-Do: la fonction tri le dataframe recu en parametre selon les variable type_sort et ascendant
    #To-Do: type_sort[V   D  DP  PTS  VRP   BP   BC  DIFF]
    #To-Do: ascendant = True(ordre decroissant), False(ordre croissant)
    # Lien utile: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
    
    return ...


def df_summary_inf(...):
    #To-Do: la fonction affiche les stats des equipes
    

def df_summary_divison(...):
    # To-Do: La fonction va classer les equipes de chaque division selon le critere recu en parametre(type_sort)
    # To-Do: a l'aide de la bibliotheque seaborn visualiser le classement de chaque division
    # Lien utile: https://seaborn.pydata.org/tutorial/axis_grids.html
    # Lien utile: https://seaborn.pydata.org/generated/seaborn.barplot.html

    
    plt.show()


def df_summary_league(...):    
    # To-Do: La fonction va classer les equipes de la ligue selon le critere recu en parametre(type_sort)
    # To-Do: a l'aide de la bibliotheque seaborn visualiser le classement des10 meilleurs equipes dela ligue
    # Lien utile: https://seaborn.pydata.org/generated/seaborn.barplot.html

    
    plt.show()
    
def df_groupby_div(...):
    # To-Do: la fonction regroupe le dataframe par division
    # Lien utile: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
    return ...

def df_secteur_div(...):
    #TODO: La fonstion affiche en secteur le pourcentage par division des 10 premiers equipes dans la ligue selon la variable
    #TODO: type_data, par exemple si type_data = "PTS", vous devez visualiser le pourcentage de points de chaques divison
    #TODO: Parmi les 10 premieres equipes
    #TODO: Trier le dataframe en utilisant la fonction df_sort_type
    #TODO: Extraite les 10 premier element du dataframe
    #TODO: Regrouper le dataframe en utilisant la fonction df_groupby_div
    # Lien utile: https://plotly.com/python/pie-charts/

    
    fig.show()



if __name__ == '__main__':
    # 1.1
    ligue_classement = lire_classement()
    
    # 1.2
    nhl_df = creer_df(ligue_classement)
    print(nhl_df)
    # 1.3
    for div in division:
        print(df_extraite_divison(nhl_df, div))
        print("\n")
        
    # 1.4.a
    nhl_df_sort_by_pts = df_sort_type(nhl_df, "PTS", False)
    print(nhl_df_sort_by_pts)
    print("\n")
    
    # 1.4.b
    nhl_div_df = df_extraite_divison(nhl_df, "Atlantic")
    nhl_div_df_sort_by_v = df_sort_type(nhl_div_df, "V", True)
    print(nhl_div_df_sort_by_v)
    
    # 1.5
    df_summary_inf(nhl_df)
    
    # 2.1
    df_summary_divison(nhl_df,"PTS", False)
    df_summary_divison(nhl_df,"V", False)
    df_summary_divison(nhl_df,"BP", False)
    
    # 2.2
    df_summary_league(nhl_df,"PTS", False)
    df_summary_league(nhl_df,"V", False)
    df_summary_league(nhl_df,"DIFF", False)
    df_summary_league(nhl_df,"DIFF", True)
    
    # 2.3.a
    df_secteur_div(nhl_df, "PTS", False)
    df_secteur_div(nhl_df, "PTS", True)
    
    # 2.3.a
    df_secteur_div(nhl_df, "V", False)
    df_secteur_div(nhl_df, "V", True)
    