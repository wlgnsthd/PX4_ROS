import os
#import csv
import pandas as pd
#pip install pandas

Dest = os.getcwd()
fileEx = r'.txt'
txt_list = [file for file in os.listdir(Dest) if file.endswith(fileEx)]

result_q = input('Do you really want to modify txt labels? (y/n) : ')
result_c = input('Select column number which you want to modify? (1 column number 0~) : ')
result_n = input('What number do you want to modify? (1 Integer 0~) : ')

if result_q == 'y':
    result_path = './new_txt'
    os.makedirs(result_path,exist_ok=True)
for i in range(len(txt_list)):
    txt_list[i]=txt_list[i][:-4]

for i in range(len(txt_list)):
    file = pd.read_csv(txt_list[i]+'.txt', sep=' ',encoding='utf-8',names=('cl','xmin','ymin','w','h'))

    file.loc[int(result_c),'cl'] = int(result_n)
    
    file.to_csv(r'new_txt/'+txt_list[i]+'.txt',sep=' ',index=False, header=False) #최종경로 변경
