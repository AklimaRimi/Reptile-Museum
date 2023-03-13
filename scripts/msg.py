import cv2
import os
import numpy as np
import pandas as pd

data=[]

csv = pd.read_csv('data/Reptil.csv')


for folder in os.listdir('augimg'):
    
    new_df = csv[csv['Scientific_Name'] == folder]


    for images in os.listdir(f'augimg/{folder}'):
        
        imgpath = f'augimg/{folder}/{images}'
        Type = new_df['Species'].values[0]
        name = new_df['Name'].values[0]
        s_n = new_df['Scientific_Name'].values[0]
        cs = new_df['Conservation_Status'].values[0]
        habi = new_df['habitat'].values[0]
        color = new_df['Color'].values[0]
        found_in = new_df['Found_In'].values[0]
        diet = new_df['Diet'].values[0]
        data.append([imgpath,Type,name,s_n,cs,habi,color,found_in,diet])
        print(f'{folder}    kaj hoitese')
    
data = pd.DataFrame(data,columns=['Image','Type','Name','Scientific Name','Conservation Status','Habitant','Color','Found In','Diet'])
data = data.sample(frac=1,random_state=42)
data.to_csv('data/final_data.csv',index=False)

