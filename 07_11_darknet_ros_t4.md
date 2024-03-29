# Custom OBJ detection with Yolov3
## Ultralytics 
##### https://medium.com/analytics-vidhya/custom-object-detection-with-yolov3-8f72fe8ced79
```
git clone https://github.com/TheCaffeineDev/YoloV3-Custom-Object-Detection.git
```
```
main_folder
│   - detect.py
│   - models.py
│   - train.py*******
│  - test.py
│  - requirements.txt
│  ...
└─── cfg
└─── conversion
    │
    └─── output***
    └─── xmls*
    │  - classes.txt**
    │  - xmltotxt.py
    │  ...
└─── data
└─── training
│ │
│ └─── images*
│ └─── labels***
│ - object.names****
│ - trainer.data*****
│ - yolov3.cfg******
│ - train_test.py*****
│
└─── utils
└─── weights
```
```
cd YoloV3-Custom-Object-Detection
pip3 install -r requirements.txt
```
### 1, put images and xmls to the folders & 2, edit classes.txt
```
# In YoloV3-Custom-Object-Detection/conversion folder
cd conversion
## python3 -m pip install transformers declxml
## sudo chmod 777 output
python3 xmltotxt.py -xml xmls -out output
```
### 3, move txt file to label folder & 4, edit object.names putting my classes
```
# In YoloV3-Custom-Object-Detection/training folder
cd ../
cd training
# Revise path
python3 train_test.py
```
### 5, edit trainer.data , classes number, train test txt path, object.names path
### 6,edit cfg file 
#### classes = n, filter = (4+1+n)x3 , no_6:batch_7:subdivision_610_603_689_696_776_783 in yolov3.cfg
##### (default layer 255 output, 85 output per anchor(4box coord+1 obj conf+80 class conf) x3)
_________________________
### 7,Training model
```
# In YoloV3-Custom-Object-Detection run
cd ../
## conda install pytorch torchvision -c pytorch 
python3 train.py --epochs 110 --data training/trainer.data --cfg training/yolov3.cfg --batch 16 --accum 1
```
#### While training, do this in another terminal
```
tensorboard --logdir=runs
```
__________________________
### Exporting weights file
#### do it in terminal
```
# convert cfg/pytorch model to darknet weights
# In YoloV3-Custom-Object-Detection
python3  -c "from models import *; convert('training/yolov3.cfg', 'weights/best.pt')"
```
_____________
### Testing
```
# In YoloV3-Custom-Object-Detection - for webcam
python3 detect.py --source 0 --weights converted.weights --cfg training/yolov3.cfg --names training/object.names --img-size 416
```
________________
________________
# Reinstall OpenCV 3
```
pkg-config --modversion opencv 
pkg-config --modversion opencv4
sudo apt-get purge libopencv* python-opencv
sudo find /usr/local/ -name "*opencv*" -exec rm {} \;
# 안지워진 폴더 삭제
# sudo rm -rf /usr/local/include/opencv
# sudo rm -rf /usr/local/include/opencv4
sudo apt autoremove -y
```
```
mkdir opencv
cd opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.0.zip
unzip opencv
unzip opencv_contrib
cd opencv-3.4.0
mkdir build
cd build
```
```
# nano
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D WITH_TBB=OFF \
-D WITH_IPP=OFF \
-D WITH_1394=OFF \
-D BUILD_WITH_DEBUG_INFO=OFF \
-D BUILD_DOCS=OFF \
-D INSTALL_C_EXAMPLES=ON \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_PERF_TESTS=OFF \
-D WITH_QT=OFF \
-D WITH_GTK=ON \
-D WITH_OPENGL=ON \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.4.0/modules \
-D WITH_V4L=ON  \
-D WITH_FFMPEG=ON \
-D WITH_XINE=ON \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D PYTHON2_INCLUDE_DIR=/usr/include/python2.7 \
-D PYTHON2_NUMPY_INCLUDE_DIRS=/usr/lib/python2.7/dist-packages/numpy/core/include/ \
-D PYTHON2_PACKAGES_PATH=/usr/lib/python2.7/dist-packages \
-D PYTHON2_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so \
-D PYTHON3_INCLUDE_DIR=/usr/include/python3.6m \
-D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/lib/python3/dist-packages/numpy/core/include/  \
-D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
-D PYTHON3_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so \
../

#xavier
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_CUDA=ON -D CUDA_ARCH_BIN="7.2" -D CUDA_ARCH_PTX="" -D WITH_CUBLAS=ON -D ENABLE_FAST_MATH=ON -D CUDA_FAST_MATH=ON -D ENABLE_NEON=ON -D WITH_GSTREAMER=ON -D WITH_LIBV4L=ON -D BUILD_opencv_python2=ON -D BUILD_opencv_python3=ON -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D BUILD_EXAMPLES=OFF -D WITH_QT=ON -D WITH_OPENGL=ON -D CUDA_NVCC_FLAGS="--expt-relaxed-constexpr" -D WITH_TBB=ON ..

```
```
# core 수에 따라 다르게 분배 (4개 코어)
make -j4
```
```
sudo make install
# 환경등록 
sudo sh -c 'echo '/usr/local/lib' > /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```
### ROS 재설치 
___________________
## !Error

#### ROS 설치시 OpenCV 4버전 자동 설치 됨 4.1.1
##### ROS 설치전
![Screenshot from 2022-07-11 14-41-36](https://user-images.githubusercontent.com/88171531/178196338-fa92f161-e173-4af5-a6d9-8d85c875bc4d.png)
##### ROS 설치후
![Screenshot from 2022-07-11 14-39-55](https://user-images.githubusercontent.com/88171531/178196163-a4c81e8e-8504-41cd-a457-c25cdde5b7dd.png)
##### ->  ROS 냅두고 OpenCV 다시설치 -> 다시 설치후 cv_bridge 설치시 4.1.1 설치되는 문제

