# ROS YOLO SORT 구현 시도
### what is SORT(Simple Online & Realtime Tracking)? 
##### https://mickael-k.tistory.com/48
__________________________
##### https://ropiens.tistory.com/189
## Darknet 별도 실행
```
roscore
```
```
rosrun uvc_camera uvc_camera_node
```
```
source ~/catkin_ws/devel/setup.bash
roslaunch darknet_ros yolo_v4.launch
```
## Published BBox tracking using Karman Filter
```
cd ~/catkin_ws/src
git clone https://github.com/mkyun2/ROS_SORT.git
```
```
# CamkeList.txt 에서 cv3_bridge & Opencv 3 Required 수정
cd ../
catkin_make
```
```
rosrun sort_ros sort_ros_node
```
## Problem ( No view and organized output )
![Screenshot from 2022-07-15 10-25-02](https://user-images.githubusercontent.com/88171531/179128381-ae04a801-2555-49f5-96c4-609b37084d20.png)
![Screenshot from 2022-07-15 10-27-26](https://user-images.githubusercontent.com/88171531/179128389-97048f73-62ee-4242-8ee6-0588abc73429.png)
### Edit CPP File
##### 근본적인 문제 : SORT를 사용해도 정확도가 올라가지만 fps의 손해가 있다. 현재 fps를 높여야하는 것에 집중해야함
_______________________
# Yolov4 각 모델 비교 
## Yolov4 model coco 적용 
![Screenshot from 2022-07-15 13-41-59](https://user-images.githubusercontent.com/88171531/179152206-dd199471-d0eb-47b8-b9e0-17aa53e1144e.png)
### (cfg batch sub 1로, width height 416)

![Screenshot from 2022-07-15 15-24-46](https://user-images.githubusercontent.com/88171531/179164445-38d22920-78ad-4409-ba0a-977564f8f68a.png)
## Yolov4 tiny model coco 적용
![Screenshot from 2022-07-15 13-39-24](https://user-images.githubusercontent.com/88171531/179151893-625c4302-44c9-4519-ae90-a374ca1277a8.png)
## Yolov3 tiny model coco 적용
![Screenshot from 2022-07-15 13-59-36](https://user-images.githubusercontent.com/88171531/179154024-1beaa54e-787f-4d8e-9890-64cfee63421b.png)

## Yolov4 csp model coco 적용 (!GPU 사용 여부 고려)
![Screenshot from 2022-07-15 13-36-21](https://user-images.githubusercontent.com/88171531/179151598-8a11be84-e97c-47e1-9360-3f17f5f5ab15.png)
#### https://github.com/WongKinYiu/ScaledYOLOv4/issues/89

![Screenshot from 2022-07-15 13-48-31](https://user-images.githubusercontent.com/88171531/179153302-bce4eb3d-2667-4e0f-b3c6-fb8b6450eae5.png)
