import cv2
import os
import numpy as np
import pandas as pd

data=[]

csv = pd.read_csv('Reptil.csv')

for folder in os.listdir('augimg'):
    i=0
    for images in os.listdir(f'augimg/{folder}'):
        imgpath = f'augimg/{folder}/{images}'
        type = csv['Species'][i]
        name = csv['Name'][i]
        s_n = csv['Scientific_Name'][i]
        cs = csv['Conservation_Status'][i]
        habi = csv['habitat'][i]
        color = csv['Color'][i]
        found_in = csv['Found_In'][i]
        diet = csv['Diet'][i]
        
        data.append([imgpath,type,name,s_n,cs,habi,color,found_in,diet])

data = pd.DataFrame(data,columns=['Image','Type','Name','Scientific Name','Conservation Status','Habitant','Color','Found In','Diet'])
data = data.sample(frac=1,random_state=42)

data.to_csv('final_data.csv',index=False)

