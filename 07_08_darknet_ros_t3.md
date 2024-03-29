# Delete ROS OpenCV 
```
sudo apt-get purge ROS-*
sudo apt-get purge gazebo*
sudo apt-get purge libopencv*
sudo rm -rf /usr/share/opencv
sudo rm -rf /usr/share/opencv2
sudo rm -rf /usr/share/opencv4
sudo apt-get autoremove
```
# OpenCV 3 reinstall
```
sudo apt-get install python2.7-dev python3-dev python-numpy python3-numpy libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev v4l-utils  libxvidcore-dev libx264-dev libxine2-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk-3-dev mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev libatlas-base-dev gfortran libeigen3-dev
sudo apt-get purge libopencv*
git clone https://github.com/jetsonhacks/buildOpenCVXavier.git
cd buildOpenCVXavier
git checkout v1.0
./buildOpenCV.sh
./removeOpenCVSources.sh
```

# ROS Melodic reinstall
```
sudo apt-get update && sudo apt-get upgrade -y
git clone https://github.com/jetsonhacks/installROSXavier
cd installROSXavier

./installROS.sh -p ros-melodic-desktop-full
./setupCatkinWorkspace.sh

sudo apt-get install ros-melodic-rqt*
sudo rosdep init
rosdep update
sudo apt-get install python-rosinstall

source /opt/ros/melodic/setup.bash
cd ~/catkin_ws/src
catkin_init_workspace

cd ~/catkin_ws
catkin_make

source ~/catkin_ws/devel/setup.bash
gedit ~/.bashrc
# export ROS_MASTER_URI=http://localhost:11311
# export ROS_HOSTNAME=129.254.81.188

roscore
```

# Yolo darknet ROS reinstall
```
cd catkin_ws/src
git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
cd ../
catkin_make -DKMAKE_BUILD_TYPE=Release
# 빌드 완료후
# darknet_ros/darknet/Makefile열어서 GPU,CUDNN, OPENCV = 1로, gencode arch=compute_72,code=sm_72\ gencode arch=compute_72,code=[sm_72,compute_72]| 변경
# darknet_ros/darknet_ros/CMakeList.txt에서도 뒷부분 똑같이 수정
# usb 카메라 설치
sudo apt install ros-melodic-uvc-camera 

# darknet_ros/darknet_ros/config/ros.yaml에서 rostopic list에서 image 토픽 확인->/camera/rgb/image_raw로 변경
# darknet_ros/darknet_ros/launch/darknet_ros에서 rostopic list에서 image 토픽 확인->/camera/rgb/image_raw로 변경, yolo version에 맞게 yolov2,yolov3넣음

# roscore 실행하기
rosrun uvc_camera uvc_camera_node
roslaunch darknet_ros darknet_ros.launch # yolov2, v2 tiny 모델일때 
roslaunch darknet_ros yolo_v3.launch # yolov3 모델일때
```
_____________________________
## !Error
![Screenshot from 2022-07-08 13-17-06](https://user-images.githubusercontent.com/88171531/177915959-07f83909-c34f-4a4f-ac20-2232722d916b.png)
### Return to reinstalling part -> OpenCV4 & YoloV4 Combination
______________________________

# Install OpenCV 4
https://qengineering.eu/install-opencv-4.5-on-jetson-nano.html
```
wget https://github.com/Qengineering/Install-OpenCV-Jetson-Nano/raw/main/OpenCV-4-6-0.sh
sudo chmod 755 ./OpenCV-4-6-0.sh
./OpenCV-4-6-0.sh

# once the installation is done...
rm OpenCV-4-6-0.sh
# just a tip to save an additional 275 MB
sudo rm -rf ~/opencv
sudo rm -rf ~/opencv_contrib
```
# Reinstall ROS Melodic
# Install Yolov4 for darknet ROS
https://github.com/Tossy0423/yolov4-for-darknet_ros
_Next Time_
