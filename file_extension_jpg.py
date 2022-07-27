import os
# Current path 
Dest = os.getcwd()
# File extension
fileEx = r'.jpg'
jpg_list = [file for file in os.listdir(Dest) if file.endswith(fileEx)]

for i in range(len(jpg_list)):
#    print(jpg_list[i])
    jpg_list[i]=jpg_list[i][:-4]
jpg_list

#to txt : Change train.txt || valid.txt
ATfile = open("train.txt","w")
for i in range(len(jpg_list)):
    ATfile.write(Dest+'/'+jpg_list[i]+'.jpg'+'\n')
ATfile.close()
