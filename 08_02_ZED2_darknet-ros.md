# Zed 2 in Jetson Xavier AGX
https://www.stereolabs.com/developers/release/
### ZED SDK설치
```
chmod +x ZED_SDK_Tegra_L4T32.7_v3.7.6.run 
./ZED_SDK_Tegra_L4T32.7_v3.7.6.run 
```
### ZED ROS wrapper 설치
```
cd ~/catkin_ws/src
git clone --recursive https://github.com/stereolabs/zed-ros-wrapper.git
cd ../
rosdep install --from-paths src --ignore-src -r -y
catkin_make -DCMAKE_BUILD_TYPE=Release
source ./devel/setup.bash
```

### ZED ROS example 설치
```
cd ~/catkin_ws/src
git clone https://github.com/stereolabs/zed-ros-examples.git
cd ../
rosdep install --from-paths src --ignore-src -r -y
catkin_make -DCMAKE_BUILD_TYPE=Release
source ./devel/setup.bash
```
#### Yolov4_zed display rviz (7fps, 98%gpu)
![Screenshot from 2022-08-02 09-39-45](https://user-images.githubusercontent.com/88171531/182267706-bfb8d529-9db2-45be-9c92-109623406a0c.png)
#### Yolov4-tiny_zed display rviz (40fps, 80%gpu)
![Screenshot from 2022-08-02 09-59-33](https://user-images.githubusercontent.com/88171531/182269488-72712373-4c90-4657-85d8-32e247dc0484.png)

________________
### darknet ros 에서 zed를 이용한 거리 표현
#### Make file에서 zed = 1 & catkin make 실시
#### !Error : built target zed_interface_msg cpp 관련
#### Solution : Makefile 140번째줄에서 주석처리 해제
