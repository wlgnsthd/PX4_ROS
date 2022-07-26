import os
# 폴더명 수정 
Dest = os.getcwd()
fileEx = r'.jpg'
jpg_list = [file for file in os.listdir(Dest) if file.endswith(fileEx)]

for i in range(len(jpg_list)):
#    print(jpg_list[i])
    jpg_list[i]=jpg_list[i][:-4]
jpg_list

#csv로 저장후 엑셀복사해서 txt로 저장
ATfile = open("train.txt","w")
for i in range(len(jpg_list)):
    ATfile.write(Dest+'/'jpg_list[i]+'.jpg'+'\n')
ATfile.close()
