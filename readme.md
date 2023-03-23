 
# Reptile Museum

# Motive
  The purpose of this project is to create an app to help people learn more about any kind of reptile around the world. It is also kid friendly. Just input an image of a reptile (such as Crocodile, Lizards, Snake, Turtle) this app will show you all the information such as `Name`, `Scientific Name`,`Type`,  generally where the reptile `Commonly found in`, `Color`, `Food Habit`, `Conservation Status`, `Habitat` in a very basic way.
  
# Machine Learning Method
  My goal is for the user to apply an input as an image and receive 8 outputs. So this is the reason I have to choose the `Multi-Target` Image Classification method as the backbone.  
  
  ### **Why did I choose Machine Learning when I can use Normal Data Structure/ Code?**
  
  If I use Data Structure / Algorithm / Explicite code, This will need huge data for individual species. Also Image Analysis is much more complex without ML. This is the reason I chose Machine Learning for Image classification.  

# Data Collection
  I collected my data with the help of `google`, `ChatGPT`.
  
1. Collected Reptile `Type` names around the world. Currently I choose Crocodile, Lizard, Snake, Turtle.<br>
2. For the individual `Type` I have collected `Name` of all species Also their `Scientific Name`, `conservation Status`,`Habitat`,`Found In`, `Color`, `Diet`. Using *Wikipedia*,*National Geographic website*, [link](https://www.crocodilesoftheworld.co.uk/conservation/conservation-status/) and *ChatGPT* I ensured, my data is Correct or not. All data I have collected manually. `108` Species information is  collected. <br>
3. According to `Name` I collected images. Basically, I scrape images from Google Photos using `Selenium`. Almost 50 images collected for each `Name`.

# Data Preprocessing and Image Augmentation

  As you can see, my dataset is small, and Google Images only has a few images for specific species, I generated more images based on the few images collected `6539`, and I use 8 types of `Augmentation`(Rotate,Brightness,Flip etc) to increase this dataset. After all of this, my current data size is `45767` . [Dataset](https://github.com/AklimaRimi/Reptile-Museum/blob/main/data/final_csv.csv)
  
# Model Training
  For the rest of the tasks like training, testing, and compression, I choose `Fastai` `Pytorch` to get better performance and time effect.
  
  For training, I use 3 types of models, `resnet50`, `resnet34`, `xresnet18deeper`, and I save the best model as `pkl` for future use.
  
  Also, I did some experiments using `batch size`. I used 3 different batch sizes to see if there was any tiny effect on the model's accuracy. <br><br>`Batch size` = 16, which made the model training process very slow and low-accurate. <br>`Batch size` = `32`, made the model training process faster with the highest accuracy. <br>`Batch size` = 64, it gave the fastest training process but was not as accurate as bs = 32.

# Final Model Selection
  As I used 3 types of models here is their best results..<br>  
   |   Model       |     Accuracy|   F1_score | Precision |  Time  |
  |---------------|-------------|-------------|-----------|--------|
  | Resnet50      |      .9981  |   0.930426  |  0.970514 |  08:20 |
  | Resnet34      |     0.998095|	0.927186	  | 0.956563	|  07:31 | 
  | xresnet18_deeper |  0.977500|	0.023208	  |  0.068224	| 05:40  |

  As `resnet50` and `resnet34` both reach `99%` Accuracy and another score is way close but `resnet34` is a little bit faster. So I chose `resnet34` for further work.

# Inside of Final Model Training/ Analysis
  For analysis on what is going on during training The model, I use `Weight and Bias` and create a dashboard. [Here it is](https://wandb.ai/aklimarimi7/Reptile-Museum?workspace=user-aklimarimi7).

# Model size Compression
  Model compression is very essential, because we as developers want to reduce or manage app size. In that case, I use  `onnx` for model size compression. It also makes faster the model.    

# Deployment
  `HuggingFace` is the platform where I deployed my project. You can see this from [here](https://huggingface.co/spaces/Rimi98/Reptile-Museum).
  
  ![](https://github.com/AklimaRimi/Reptile-Museum/blob/main/output_images/hf.png)

# Interface
  As this app is educational app, I've decided to make it free for all. So I made a simple `UI` using `Flask` and rendered it on the `render.com` website. This website is free with conditions.<br><br>Here is my app [link](reptile-museum.onrender.com/).
  
  ![](https://github.com/AklimaRimi/Reptile-Museum/blob/main/output_images/front.png)
  
  ![](https://github.com/AklimaRimi/Reptile-Museum/blob/main/output_images/back.png)
  
   * The `background image` of this website is generated using `Stable Diffusion`. An AI that generates unseen images using "promt" The promte is:  <h3>night view green Amazon deep forest with reptile anime , realistic,Cartoon, mdjrny-v4 style, HQ</h3>
   * Here, I also used `Google Text To Speech` AI for kids who cannot read but have a curious mind and want to know about `Reptile`. Audio generates in `Real Time`  

# Problem That I've faced and How did I Overcome 
   Of course, I've faced so many obstacles to building this website.<br><br>First of all, set up the `Dataloader`. There are a few resources that I found for `Multi-Target` Image classifier. I've experimented in a lot of ways and finally `MultiCategoryBlock()` with the parameter `add_na = True`, this is for `Multi-Target` classification, but I believe this will also work for regression.<br>Secondly, I messed up to choose the right metric(s), finally I used `accuracy_multi`. This metric works not only well for `multi-label` classification but also  `Multi-Target` classification. I also used `F1_score` and `Precision` for a better understanding of my model.
  
  
 # Conclusion
   I have completed this project like I wanted. If you want to develop more just send me a pull request. Thanks.



