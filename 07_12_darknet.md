# Yolov3 Custom Training 
### https://keyog.tistory.com/6?category=879585
## Install Cuda
## Install Darknet
```
git clone https://github.com/pjreddie/darknet.git
cd darknet

gedit Makefile
# GPU=1 CUDNN=1(오류시 0) OPENCV=1(오류시 0) OPENMP=0 DEBUG=0

gedit examples/detector.c
#if(i%10000==0 || (i < 1000 && i%100 == 0)){ -> if(i%1000==0){ 로 변경하여 1000번 반복에 한번씩 weight출력하도록함

make
```
## Optional Test (OpenCV 설치조건)
```
wget https://pjreddie.com/media/files/yolov3.weights
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights
```
## cfg수정
```
gedit cfg/yolov3.cfg
```
```
# 수정 1 : width height 608 608 -> 416 416, batch size 조절 (gpu)
[net]
# Testing
# batch=1
# subdivisions=1
# Training
batch=64
subdivisions=16
width=416
height=416
channels=3
momentum=0.9
decay=0.0005
angle=0
saturation = 1.5
exposure = 1.5
hue=.1

learning_rate=0.001
burn_in=1000
max_batches = 500200
policy=steps
steps=400000,450000
scales=.1,.1
```
```
# 수정 2 : ctrl + f로 yolo 찾은 다음 위 아래 filter(=(classes+5)*3), classes 3개 수정
[convolutional]
size=1
stride=1
pad=1
filters=60
activation=linear


[yolo]
mask = 0,1,2
anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
classes=15
num=9
jitter=.3
ignore_thresh = .7
truth_thresh = 1
random=1
```
## Put xmls into xmls folder and make it yolov3 label
### path : conversion/xmls & conversion/output
```
python3 conversion/xmltotxt.py
```
________________________
## Put images(jpg) and labels(txt) into "dataset" folder
### path : customs/dataset
__________________
## Make train.txt and validation.txt, 7:3
### path : customs/train.txt & customs/valdiation.txt 
```
python3 customs/train_val.py
```
## Make custom.names and custom.data
### path : customs/custom.name & custom/custom.data
```
truck
ladder
```
```
classes= 2
train  = custom/train.txt
valid  = custom/validation.txt
names = custom/custom.names
backup = backup/
```
## Pretrain model 다운로드
```
wget https://pjreddie.com/media/files/darknet53.conv.74
```
## Train
```
./darknet detector train custom/custom.data custom/custom_yolov3.cfg darknet53.conv.74 | tee backup/train.log
```
```
# 순서대로 iteration : loss(iou), loss(classify), learning rate, iteration time, 훈련 이미지 수
grep "avg" backup/train.log
```
