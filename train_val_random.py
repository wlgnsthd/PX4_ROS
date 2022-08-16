# python3
pip install numpy
import glob, os, shutil
import numpy as np

# put your own path here
dataset_path = './'
# Percentage of images to be used for the validation set
percentage_val = 20;

# Create and/or truncate train.txt and validation.txt
file_train = open('train.txt', 'w')  
file_val = open('valid.txt', 'w')

# Make directory train/valid
train_new_name = '/train_new'
valid_new_name = '/valid_new'
os.makedirs(dataset_path+train_new_name,exist_ok=True)
os.makedirs(dataset_path+valid_new_name,exist_ok=True)

# Populate train.txt and validation.txt
counter = 1  
index_val = round(100 / percentage_val)  
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_val+1:#valid path
        counter = 1
        shutil.copy(dataset_path  + title + '.jpg', dataset_path + valid_new_name  )
        shutil.copy(dataset_path  + title + '.txt', dataset_path + valid_new_name  )

    else:# train path
        shutil.copy(dataset_path  + title + '.jpg', dataset_path + train_new_name  )
        shutil.copy(dataset_path  + title + '.txt', dataset_path + train_new_name  )
        counter = counter + 1
