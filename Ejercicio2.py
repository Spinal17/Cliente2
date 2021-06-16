# -*- coding: utf-8 -*-
import pandas as pd
import sys 
import numpy as np

def Cargardatos(fichero: str) -> pd.DataFrame:
    
    try:
        titanic = pd.read_csv(fichero, index_col=0)
        print('Dimensiones:', titanic.shape)
        print('Número de elemntos:', titanic.size)
        print('Nombres de columnas:', titanic.columns)
        print('Nombres de filas:', titanic.index)
        print('Tipos de datos:\n', titanic.dtypes)
        return titanic
    except:
        sys.exit("Error al abrir el archivo")


def MostrarInformacion( data: pd.DataFrame) -> pd.DataFrame:
    
    data.dropna(subset=['Age'])
    data.dropna(subset=['Cabin'])
    data['Young'] = data['Age'] < 18
    print(data['Survived'].value_counts()/data['Survived'].count() * 100)    
    print(data.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])
    print(data.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)
    return data
    
def HacerMatrizN(fichero: str) -> np.load:    
    data = np.loadtxt(fichero, delimiter=";",skiprows=2, dtype="str")
    return data 