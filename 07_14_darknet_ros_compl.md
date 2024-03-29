# Yolov4 darknet ROS
### !Error
### yolov3.cfg weight를 yolov4로 바꾸는 것만으로는 구현 불가
```
cd catkin_ws
git clone --recursive https://github.com/Tossy0423/yolov4-for-darknet_ros
cd ../
# Makefile CMakefileList.txt 수정
catkin_make -DCMAKE_BUILD_TYPE=Release
```

_______________________________
#### !Error
![Screenshot from 2022-07-14 09-33-40](https://user-images.githubusercontent.com/88171531/178859817-c16698a5-77fd-42d0-af8c-fc6c7f954e68.png)
##### OpenCV 4를 설치해야 하는 것으로 예상됨 : cv bridge를 우선 수정
``` sudo apt-get purge ros-melodic-cv-bridge
sudo apt-get install ros-melodic-cv-bridge
```
##### 재시도 -> 실패 : opencv 4로 재설치 
```
sudo apt-get update
sudo apt-get install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt-get install -y python2.7-dev python3.6-dev python-dev python-numpy python3-numpy
sudo apt-get install -y libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev
sudo apt-get install -y libv4l-dev v4l-utils qv4l2 v4l2ucp
sudo apt-get install -y curl

mkdir opencv4
cd opencv4
curl -L https://github.com/opencv/opencv/archive/4.5.5.zip -o opencv-4.5.5.zip
curl -L https://github.com/opencv/opencv_contrib/archive/4.5.5.zip -o opencv_contrib-4.5.5.zip
unzip opencv-4.5.5.zip
unzip opencv_contrib-4.5.5.zip
cd opencv-4.5.5/
 
 
echo "** Building..."
mkdir release
cd release/
cmake -D WITH_CUDA=ON \
      -D WITH_CUDNN=ON \
      -D CUDA_ARCH_BIN="7.2" \
      -D CUDA_ARCH_PTX="" \
      -D OPENCV_GENERATE_PKGCONFIG=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-${version}/modules \
      -D WITH_GSTREAMER=ON \
      -D WITH_LIBV4L=ON \
      -D BUILD_opencv_python2=ON \
      -D BUILD_opencv_python3=ON \
      -D BUILD_TESTS=OFF \
      -D BUILD_PERF_TESTS=OFF \
      -D BUILD_EXAMPLES=OFF \
      -D CMAKE_BUILD_TYPE=RELEASE \
      -D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
      -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j$(nproc)
sudo make install
sudo ldconfig
```
________________________________
### Error
![Screenshot from 2022-07-14 11-28-46](https://user-images.githubusercontent.com/88171531/178885090-c52f39fb-06a0-40a3-8a45-c80ba610ae61.png)
https://github.com/Tossy0423/yolov4-for-darknet_ros/issues/13
________________________________
## Conclusion
###  ros- opencv3 - cv3 bridge - https://github.com/Tossy0423/yolov4-for-darknet_ros 
![Screenshot from 2022-07-14 16-12-11](https://user-images.githubusercontent.com/88171531/178923839-2c95bfb1-0a4e-4db7-9540-2db3584815ac.png)
