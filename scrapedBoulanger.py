# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 09:56:30 2018

@author: Jihane Bouhammada
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrapBoulanger(url):
    # get the link of Boulanger
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # get the price and the caracteristics of laptop on the first page of Boulanger
    results = soup.find_all('ul', attrs={'class':'bestpoints'})
    #print(firstResult = results[0])
    
    # get the results 
    rResults = []
    for i in range(len(results)):
        rResults.append(str(results[i].text).replace('\n', ';').replace(' - ', ';').split(';'))  
    
    # create a dataset
    laptops = []  
    for result in rResults:  
        taille_ecran = result[1]
        HD = result[2]
        poids = result[3]
        marque = result[5]
        memoire = result[6]
        disque = result[-3]
        laptops.append((taille_ecran, HD, poids, marque, memoire, disque))
    
    # create a dataframe
    dfLaptop = pd.DataFrame(laptops, columns=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'])  
    
    return dfLaptop

def toCSV(df, nameCSV):
    # get the dataset
    df.to_csv(nameCSV, index=False, encoding='utf-8')
     
    # show the dataframe
    #df = pd.read_csv('nameCSV.csv', encoding='utf-8')
    #res = print(df.head())
    #print(df.head())
    #print(df.tail())

res1 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables")
res2 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=2")
res3 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=3")
res4 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=4")
res5 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=5")
res6 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=6")
res7 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=7")
res8 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=8")
res9 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=9")
res10 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage=10")
res11 = scrapBoulanger("https://www.boulanger.com/c/tous-les-ordinateurs-portables?numPage11")

# join the different dataframes
#res12 = res1.join(res2)
res12 = pd.merge(res1, res2, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res13 = pd.merge(res12, res3, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res14 = pd.merge(res13, res4, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res15 = pd.merge(res14, res5, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res16 = pd.merge(res15, res6, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res17 = pd.merge(res16, res7, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res18 = pd.merge(res17, res8, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res19 = pd.merge(res18, res9, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res110 = pd.merge(res19, res10, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')
res = pd.merge(res110, res11, on=['taille_ecran', 'HD', 'poids', 'marque', 'memoire', 'disque'], how='outer')


#print(len(res))
#print(res.head())

#toCSV(res, 'laptop_boulanger.csv')