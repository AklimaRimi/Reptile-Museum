from flask import Flask, render_template,request,redirect,url_for
import requests
from PIL import Image
import json
from werkzeug.utils import secure_filename
import os
from fastai.vision.all import load_learner
from fastai import *
import torch
import pathlib 
import pandas as pd
from gtts import gTTS




temp = pathlib.PosixPath 
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
UPLOAD_FOLDER = 'flask/static/upload/' 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods = ['GET','POST'])
def main_page():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            print(filename)
            image.save(f'{UPLOAD_FOLDER}{filename}')
            # print(image)
            x,y,aud = api(f'{UPLOAD_FOLDER}{filename}')
            audio = gTTS(text=aud, lang="en", slow=False)
            
            audio.save(f'flask/static/audio/{filename}.mp3')
            
            return render_template('home_page.html',label = x,value=y,image=f'upload/{filename}',audio = f'audio/{filename}.mp3')
        return render_template('home_page.html',label = '',value='',image='', audio='')
    else:
        return render_template('home_page.html',label = '',value='',image='',audio='')

def api(path):  
    model_path  = 'flask/multi_target_resnet34.pkl'
    helper_csv  = 'flask/info.csv'
    df =  pd.read_csv(helper_csv)
    model = load_learner(model_path)
    pred,_,probability = model.predict(path)
    arr = ['Species','Scientific_Name', 'Name', 'Conservation_Status', 'Color', 'habitat', 'Found_In', 'Diet']
    vals = ['','','','','','','','']
    for x in pred:
        val = df[df['values'] == x]['columns'].values[0]
        ind = arr.index(val)
        vals[ind] = x
        
    aud = f'You\'re Image animal {arr[0]} is {vals[0]}.{arr[1]} is {vals[1]}.{arr[2]} is {vals[2]}.{arr[3]} is {vals[3]}.{arr[4]} is {vals[4]}.{arr[5]} is {vals[5]}.{arr[6]} is {vals[6]}.{arr[7]} is {vals[7]}'
    return arr,vals, aud

if __name__ == '__main__':
    app.run()