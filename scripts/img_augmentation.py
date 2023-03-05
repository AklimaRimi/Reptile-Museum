import cv2
import os
import numpy as np

for folder in os.listdir('Images'):
    if folder.find('py') == -1:
        os.mkdir(f'augimg/{folder}')
        for images in os.listdir(f'Images/{folder}'):            
            
            img = cv2.imread(f'Images/{folder}/{images}')
            height, width = img.shape[:2]
            rotation_matrix = cv2.getRotationMatrix2D((width/2,height/2),20,.5)
            rotated_image = cv2.warpAffine(img,rotation_matrix,(width,height))

            bright = np.ones(img.shape , dtype="uint8") * 50
            brightincrease = cv2.add(img,bright)
            
            flip = cv2.flip(img,3)
            flip2 = cv2.flip(img,2)
            flip3 = cv2.flip(img,1)
            flip4 = cv2.flip(img,0)
            flip5 = cv2.flip(img,-1)
            
            
            cv2.imwrite(f'augimg/{folder}/orgi-{images}', img)
            cv2.imwrite(f'augimg/{folder}/x{images}', rotated_image)
            cv2.imwrite(f'augimg/{folder}/y{images}', brightincrease)
            cv2.imwrite(f'augimg/{folder}/z{images}', flip)
            cv2.imwrite(f'augimg/{folder}/a{images}', flip2)
            cv2.imwrite(f'augimg/{folder}/b{images}', flip3)
            cv2.imwrite(f'augimg/{folder}/c{images}', flip4)
            cv2.imwrite(f'augimg/{folder}/d{images}', flip5)
   
cv2.waitKey(0)
cv2.destroyAllWindows()