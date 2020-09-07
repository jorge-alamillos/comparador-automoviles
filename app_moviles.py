import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

#import csv
l_items = "output/itera.csv"
mobiles = pd.read_csv(l_items)

def bestPhone():
    """
    OBJECTIVE
    The purpose of this function is to return the appropriate phone to the budget that the user has previously entered.
    INPUT
    This function does not require inputs when it is called.
    USE
    1. Enter your maximum budget in figures
    2. Enter your minimum budget in figures (0 if you do not have a minimum budget)
    """

   
    while True:
        try:
            #Registring max and min budget
            maxbudget = input("What is you max budget?\n")
            minbudget = input("And your min budget? (Insert 0 if you do not have a minimun budget)\n")
            #Filtering the 10 best rated phones with lowest price
            selection =  mobiles[(mobiles["Price"]<= int(maxbudget)) & (mobiles["Price"]>= int(minbudget))].sort_values("rating",ascending=False).reset_index().head(10)
            selection_by_price = selection.sort_values("Price",ascending=False)
            selection_by_rating = selection.sort_values("rating",ascending=False)
            #If parameters do not get any match 
            if (len(selection)) == 0:
                return "Sorry, there are no phones with these parameters, try again."
            #Returning the recommendation
            else:
                recomendation = selection.sort_values(["rating","Price"],ascending=[False,True]).head(1)
                recomendationStr = str(selection.sort_values(["rating","Price"],ascending=[False,True]).head(1)["title"]).partition("\n")[0]
                display(selection[["Brand","Model","Price","rating"]])
                
                #Plotting
                plt.figure(figsize = (12,5))
                plt.subplot(1,2,1) 
                sns.barplot(x=selection_by_rating["Model"],y=selection_by_rating["rating"]).set(title='Rating by model', xlabel='Model', ylabel='Rating') 
                plt.xticks(rotation=45)                                      
                plt.subplot(1,2,2)
                sns.barplot(x=selection_by_price["Model"],y=selection_by_price["Price"]).set(title='Price by model', xlabel='Model', ylabel='Price')  
                plt.xticks(rotation=45)   

                print(f'Taking your budget, we recommend you to buy this model:{recomendationStr[5:]}')
                print(f'Find the purchase link here:{recomendation.url}')
                
                

            break
        #In case input is not a int/float
        except:
            print("Sorry, input must be a number")

