import pandas as pd
import os
import numpy as np
import seaborn as sns

def import_df(x):
    return pd.read_csv(x)

def show_df(df,rows=5):
        return display(df.head(rows))


def show_empty(df):
    """
    OBJECTIVE
    The purpose of this function is showing emptu rows.
    INPUT
    This function requires the df
    USE
    1. Call the function indicating the input indicated above
    """   
    is_NaN = df.isnull()
    return df[is_NaN.any(axis=1)]
    
def delete_by(df,column,value):
    """
    OBJECTIVE
    The purpose of this function is deleting a row from a df.
    INPUT
    This function requires:(df,column,value)
     - df where column will be deleted
     - column to delete
     - value in rows to be deleted
    USE
    1. Call the function indicating the inputs indicated above
    """   
    indexNames = df[df[column] == value].index
    return df.drop(indexNames, inplace=True)   

def precios_marca(df):
    """
    OBJECTIVE
    The purpose of this function is to return the distribution of prices by brand on a candlestick chart.
    INPUT
    This function requires an input DataFrame.
    USE
    1. Call the function indicating the desired dataframe
    """

    while True:
        try:
            marca = input("Choose a brand\nBrands available:\nXiaomi\nHUAWEI\nSony\nOnePlus\nGoogle\nMotorola\nSamsung\nNokia\nASUS\nApple\n")
            m = df[df["Brand"]== marca]
            display(m.Price.describe().reset_index())
            graphic = sns.boxplot(x='Price',y='Brand',data=m ,palette='rainbow').set(title=f'Estadísticas sobre el precio de {marca}')
            return graphic
        except:
            return "Non listed brand"

def ratings_marca(df):
    """
    OBJECTIVE
    The purpose of this function is to return the distribution of ratings by brand on a candlestick chart.
    INPUT
    This function requires an input DataFrame.
    USE
    1. Call the function indicating the desired dataframe
    """
    
    while True:
        try:
            marca = input("Choose a brand\nBrands available:\nXiaomi\nHUAWEI\nSony\nOnePlus\nGoogle\nMotorola\nSamsung\nNokia\nASUS\nApple\n")
            m = df[df["Brand"]== marca]
            display(m.rating.describe().reset_index())
            graphic = sns.boxplot(x='rating',y='Brand',data=m ,palette='rainbow').set(title=f'Estadísticas sobre los ratings de {marca}')
            return graphic 
        except:
            return "Non listed brand"

def ratings_price(df):
    """
    OBJECTIVE
    The purpose of this function is to return the distribution of ratings and prices on a jointplot.
    INPUT
    This function requires an input DataFrame.
    USE
    1. Call the function indicating the desired dataframe
    """
    while True:
        try:
            marca1 = input("Choose a brand\nBrands available:\nXiaomi\nHUAWEI\nSony\nOnePlus\nGoogle\nMotorola\nSamsung\nNokia\nASUS\nApple\n")
            m = df[df["Brand"]== marca1]
            graphic = sns.jointplot(x='Price',y='rating',data=m).set(title=f'Ratings-Precio de {marca1}')
            return graphic
        except:
            return "Non listed brand"