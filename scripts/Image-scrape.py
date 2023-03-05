from fastbook import *
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
import requests
import base64


driver = webdriver.Chrome()

names  =pd.read_csv('Reptil.csv')['Scientific_Name'].values.tolist()

i =0
links = pd.read_csv('Reptil.csv')['Image Link'].values.tolist()

img =[]

for ind,name in enumerate(names):
    os.mkdir(f'Images/{name}')
    print(i)

    driver.get(links[i])
    time.sleep(2)
    for scroll in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    img_links = driver.find_elements(By.XPATH,'//a[@class="wXeWr islib nfEiy"]')
    j=0
    for img_link in img_links:
        lnk = img_link.find_element(By.TAG_NAME,'img').get_attribute('src')
        try:
            try:
                decodeit = open(f'Images/{name}/{name}{j}.jpeg', 'wb')
                decodeit.write(base64.b64decode((lnk[22:])))
                decodeit.close()
            except:
                img = Image.open(requests.get(lnk, stream = True).raw)
                img.save(f'Images/{name}/{name}{j}.jpeg')
            j+=1
        except:
            continue
    
    i+=1    
    

df = pd.DataFrame(img,columns=['img'])
df.to_csv('images.csv',index=False)
    
driver.close()
