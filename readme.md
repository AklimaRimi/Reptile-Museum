
# Reptile Museum

# Motive
  Motive of this project is to create an app for know better about any kind of reptile around the world. It is also kid friendly. Just input an image of a reptile( such as Crocrodile, Lizards, Snake, Turtle) this app will show you all the information such as `Name`, `Scientific Name`,`Type`,  generally where the reptile `Live`, `Color`, `Food Habit`, `Conservation Status`, `Habitat` in a basic way.
  
# Machine Learning Method
  My goal is to user apply a input as Image and get 8 outputs. So this the reason I have to choose `Multi-Target` Image Classification method as Backbone. 
  
  ### **Why did I choose Machine Learning when I can use Normal Data Stucture/ Code?**
  
  If I use Data Structure / Algorithm / Explicite code, This will need huge data for indivisual species. Also Image Analysis is much complex without ML. This is the reason I chose Machine Learning for Image classification.  

# Data Collection
  I Collected my data with the help of `google`, `ChatGPT`.
  
  1. Collected Reptile `Type` names Around the world. Currently I choose Crocodile, Lizard, Snake, Turtle.
  2. For the indivisual `Type` I have collected `Name` of all species Also their `Scientific Name`, `conservation Status`,`Habitat`,`Found In`, `Color`, `Diet`. Using *Wikipidea*,*National Geograph website*, [link](https://www.crocodilesoftheworld.co.uk/conservation/conservation-status/) and *ChatGPT* I ensured, my data is Correct or not. All data I have collected manually. `108` Species information are  collected.
  3. According `Name` I collected Images. Basically, I scrape Images from Google photo using `Selenium`. Almost 50 images collected for each `Name`.

# Data Preprocessing and Increase Dataset

  As you find out that my dataset is tiny and Google image contains few of images for particular species, I generate more Images based on few images, I use 8 types of `Agmentation`(Rotate,Brightness,Flip etc) to increase this dataset and after all of this my current data size is `45767` . [Dataset](https://github.com/AklimaRimi/Reptile-Museum/blob/main/data/final_csv.csv)
  
# Model Training
  For the rest of the task like training, testing, compression I choose `Fastai` `Pytorch` for to get better performance and time effiect.
  
  for training I use 3 types of models, `resnet50`, `resnet34`, `xresnet18deeper`, and I save the best model as `pkl` for future use.

# Final Model Selection

# Inside of Final Model Training/ Analysis

# Model size Compression

# Deployment

# Interfence 

# Problem That I've faced

# How did I Overcame roadblocks

# Conclusion






















 , Wikipedia , Openai

weight and bias dashboard: https://api.wandb.ai/links/aklimarimi7/xmsibkbh
