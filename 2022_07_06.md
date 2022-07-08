## ROS 설치
```
sudo apt-get install python-pip
sudo pip install -U rosdep
sudo rosdep init
rosdep update
```

## OpenCV 3.4 설치 (기존 4.4 버전 지우고 재설치, YoloV3호환)
```
sudo apt-get purge libopencv*
git clone https://github.com/jetsonhacks/buildOpenCVXavier.git
cd buildOpenCVXavier
git checkout v1.0
./buildOpenCV.sh
./removeOpenCVSources.sh
```
__________________________________________
### !Error
![Screenshot from 2022-07-06 17-56-55](https://user-images.githubusercontent.com/88171531/177512047-91e7dac3-d3c2-4560-a0cf-daf0d9c60688.png)
No Storage Space
___________________________________________
## YOLO 설치 (Make file) Stopped
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
```

## YOLO 세팅
```
# darknet_ros/darknet_ros/config/ros.yaml에서 rostopic list에서 image 토픽 확인->/camera/rgb/image_raw로 변경
# darknet_ros/darknet_ros/launch/darknet_ros에서 rostopic list에서 image 토픽 확인->/camera/rgb/image_raw로 변경, yolo version에 맞게 yolov2,yolov3넣음
```

## YOLO 실행하기
```
# roscore 실행하기
rosrun uvc_camera uvc_camera_node
roslaunch darknet_ros darknet_ros.launch # yolov2, v2 tiny 모델일때 
roslaunch darknet_ros yolo_v3.launch # yolov3 모델일때
```

### launch, yaml 파일 분석



