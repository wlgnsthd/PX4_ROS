__________________________________________
#### !Error
![Screenshot from 2022-07-06 17-56-55](https://user-images.githubusercontent.com/88171531/177512047-91e7dac3-d3c2-4560-a0cf-daf0d9c60688.png)
___________________________________________

## Try 1
### 불필요한 패키지 제거
```
dpkg -l
dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n | tail -n 100 # Sort in descending order
# ROS 관련 패키지
sudo apt-get purge ROS-*
sudo apt-get purge gazebo*

```
### 파티션 생성
```
sudo fdisk -l # 디스크 목록
sudo fdisk /dev/nvme0n1 # fdisk cil 실행 m : 도움말, n : 새파티션, p : 주요파티션 등록확인, w : 종료

sudo apt-get update
sudo apt-get upgrade git
sudo apt-get install git
git clone https://github.com/jetsonhacks/rootOnNVMe #홈 디렉토리에 클론

cd rootOnNVMe
./copy-rootfs-ssd.sh
./setup-service.sh

sudo reboot

df -h # 디스크 공간 확인
```
![Screenshot from 2022-07-07 10-33-56](https://user-images.githubusercontent.com/88171531/177673167-8e1b9c93-b414-4005-a100-48f27b89b2eb.png)

## Solved
___________________________________________

### Jetson Status Check
```
sudo -H pip3 install -U jetson-stats
sudo jtop
cheese #캠동작
```

## RE : OpenCV 3.4 설치 (기존 4.4 버전 지우고 재설치, YoloV3호환)
```
sudo apt-get purge libopencv*
git clone https://github.com/jetsonhacks/buildOpenCVXavier.git
cd buildOpenCVXavier
git checkout v1.0
./buildOpenCV.sh
./removeOpenCVSources.sh
```
![스크린샷, 2022-07-07 12-27-40](https://user-images.githubusercontent.com/88171531/177684453-348a3772-0cc2-45a0-99c4-0ebaa00bc77e.png)

## YOLO 설치 (Make file)
```
cd catkin_ws/src
git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
cd ../
catkin_make -DKMAKE_BUILD_TYPE=Release
```
___________________________________________
### !Error
![스크린샷, 2022-07-07 13-01-22](https://user-images.githubusercontent.com/88171531/177688175-a3d0bbdf-8d2d-424a-a52b-f0cc5b6fe46f.png)
### Solution
![스크린샷, 2022-07-07 13-16-59](https://user-images.githubusercontent.com/88171531/177690141-f12d077e-5a85-4a70-93f6-99c892a88e85.png)
```
cd /opt/ros/melodic/share/cv_bridge/cmake
sudo gedit cv_bridgeConfig.cmake
# revise to texts written above 
```
___________________________________________

### !Error
![스크린샷, 2022-07-07 13-21-25](https://user-images.githubusercontent.com/88171531/177690805-65bfb227-09d4-4a50-8b2c-de2a0796cf5c.png)
No accurate solution -> Next Step
___________________________________________

### !Error
![스크린샷, 2022-07-07 13-44-09](https://user-images.githubusercontent.com/88171531/177693134-8c14bde9-c677-4d8e-9865-2e572a94f119.png)
### Solution 
``` 
sudo gedit ~/.bashrc
# IP & host -> localhost edit
```
Restart with /home ...
___________________________________________
### Reinstall ROS in Xavier
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
![스크린샷, 2022-07-07 16-12-07](https://user-images.githubusercontent.com/88171531/177713775-a653a98d-91b4-40b9-b93f-4a6df72d3f55.png)

_________________________
## !Error
```
cd catkin_ws
catkin_make -DCMAKE_BUILD_TYPE=Release
```
![스크린샷, 2022-07-07 17-23-28](https://user-images.githubusercontent.com/88171531/177727354-41d95898-5982-40a0-b354-84542366e55f.png)
```
rosdep install --from-paths catkin_ws/src --ignore-src
```
### Still error
___________________________________________
