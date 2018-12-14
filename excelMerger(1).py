#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import glob
import os


# In[14]:


#os.listdir(".")


# In[15]:


#Prendo i file da unire nella cartella e li metto in una lista
fileSingoli = glob.glob("*.xlsx")
fileSingoli


# In[17]:


#Check on total number of elem.
tot = len(fileSingoli)
print(tot)


# In[18]:


#Filename cleaning: remove ".xlsx"
sheetNameList = [i.split('.')[0] for i in fileSingoli]
sheetNameList


# In[19]:


#outputfile 
writer = pd.ExcelWriter('output.xlsx')


# In[20]:


#lista vuota per salvare i file
listaDf = []


# In[4]:


# #test test
#for i in range(len(fileSingoli)):
#     dati = pd.read_excel(fileSingoli[i],header=None)
#     dati.to_excel(writer,sheetNameList[i], index=False, header=False)
#     print("Processing: " ,sheetNameList[i])
#     writer.save()


# In[ ]:


#carica i file in un df li mette in una lista e li scrive e poi li toglie dalla lista (tentativo di salvare memoria)
for i in range(len(fileSingoli)):
    dati = pd.read_excel(fileSingoli[i],header=None)
    listaDf.append(dati)
    listaDf[0].to_excel(writer,sheetNameList[i], index=False, header=False)
    print("Processing: " ,sheetNameList[i], " ",i+1,"/",tot )
    del(listaDf[0])
#finito il ciclo scrivo.    
writer.save()    


# In[3]:





# In[ ]:





# In[ ]:




