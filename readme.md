 
# Reptile Museum

# Motive
  The purpose of this project is to create an app to know better about any kind of reptile around the world. It is also kid friendly. Just input an image of a reptile( such as Crocodile, Lizards, Snake, Turtle) this app will show you all the information such as `Name`, `Scientific Name`,`Type`,  generally where the reptile `Live`, `Color`, `Food Habit`, `Conservation Status`, `Habitat` in a basic way.
  
# Machine Learning Method
  My goal is for the user to apply an input as an image and receive 8 outputs. So this is the reason I have to choose `Multi-Target` Image Classification method as Backbone. 
  
  ### **Why did I choose Machine Learning when I can use Normal Data Structure/ Code?**
  
  If I use Data Structure / Algorithm / Explicite code, This will need huge data for individual species. Also Image Analysis is much more complex without ML. This is the reason I chose Machine Learning for Image classification.  

# Data Collection
  I Collected my data with the help of `google`, `ChatGPT`.
  
  1. Collected Reptile `Type` names Around the world. Currently I choose Crocodile, Lizard, Snake, Turtle.
  2. For the individual `Type` I have collected `Name` of all species Also their `Scientific Name`, `conservation Status`,`Habitat`,`Found In`, `Color`, `Diet`. Using *Wikipedia*,*National Geographic website*, [link](https://www.crocodilesoftheworld.co.uk/conservation/conservation-status/) and *ChatGPT* I ensured, my data is Correct or not. All data I have collected manually. `108` Species information is  collected.
  3. According to `Name` I collected Images. Basically, I scrape Images from Google photos using `Selenium`. Almost 50 images collected for each `Name`.

# Data Preprocessing and Increase Dataset

  As you can see, my dataset is small, and Google Images only has a few images for specific species, I generated more Images based on few images, I use 8 types of `Augmentation`(Rotate,Brightness,Flip etc) to increase this dataset and after all of this my current data size is `45767` . [Dataset](https://github.com/AklimaRimi/Reptile-Museum/blob/main/data/final_csv.csv)
  
# Model Training
  For the rest of the tasks like training, testing, compression I choose `Fastai` `Pytorch` to get better performance and time effect.
  
  For training I use 3 types of models, `resnet50`, `resnet34`, `xresnet18deeper`, and I save the best model as `pkl` for future use.

# Final Model Selection
  As I use 3 types of models here is their best results..<br>  
   |   Model       |     Accuracy|   F1_score | Precision |  Time  |
  |---------------|-------------|-------------|-----------|--------|
  | Resnet50      |      .9981  |   0.930426  |  0.970514 |  08:20 |
  | Resnet34      |     0.998095|	0.927186	  | 0.956563	|  07:31 | 
  | xresnet18_deeper |  0.977500|	0.023208	  |  0.068224	| 05:40  |

  As `resnet50` and `resnet34` both reach `99%` Accuracy and another score is way close but `resnet34` is a little bit faster. So I chose `resnet34` for further work.

# Inside of Final Model Training/ Analysis
  For analysis on what is going on during training The model, I use `Weight and Bias` and create a dashboard. [Here it is](https://api.wandb.ai/links/aklimarimi7/xmsibkbh).

# Model size Compression
  Model Compression is very essential, because we as developers want to reduce or manage app size. In that case, I use  `onnx` for model size compression. It also makes faster the model.  

# Deployment
  `HuggingFace` is the platform where I deployed my project. You can see this from [here](https://huggingface.co/spaces/Rimi98/Reptile-Museum).
  
  ![](https://github.com/AklimaRimi/Reptile-Museum/blob/main/output_images/hf.png)

# Interference 
  As this app is an educational app, I've decided to make it free for all. So I made a simple `UI` using `Flask` and rendered it on the `render.com` website. This website is free with conditions. 
  
  ![](https://github.com/AklimaRimi/Reptile-Museum/blob/main/output_images/front.png)
  
  ![](https://github.com/AklimaRimi/Reptile-Museum/blob/main/output_images/back.png)
  
   * The `background image` of this website is generated using `Stable Diffusion`. An AI that generates Unseen Images Using `Promote`.
   * Here I also used `Google Text To Speech` AI for kids who can not read but has curious mind to know about `Reptile`. Audio generates in `Real Time`  

# Problem That I've faced and How did I Overcame roadblocks
  Of course, I've faced so many obstacles to build this website. 
  
  First of all, set up the `Dataloader`. There are a few resources that I found for `Multi-Target` Image classifier. I've experimented a lot of ways and finally `MultiCategoryBlock()` with the parameter `add_na = True`, this is for `Multi-Target` classification, but I believe this will also work for Regression.
  
  Secondly, I messed up to choose the right metric(s), finally I used `accuracy_multi`. This metric works not only good for `multi-label` classification but also  `Multi-Target` classification. I also used `F1_score` and `Precision` for better understanding about my model.
  
  
 # Conclusion
   I have completed this project like I wanted. If you want to develop more just send me a pull request. Thanks.



