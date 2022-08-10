![화면 캡처 2022-08-10 094105](https://user-images.githubusercontent.com/88171531/183786294-81c00f4b-76c4-45ce-a503-aced832469f2.png)

## CSP Training Second Try
![화면 캡처 2022-08-10 093437](https://user-images.githubusercontent.com/88171531/183785162-f388cfbd-279d-4579-b7d3-7d9091b4cfb2.png)
https://github.com/WongKinYiu/ScaledYOLOv4/issues/13
##### yolov4x-mish.cfg 사용하거나 new coordinate = 0 적용하여 학습
##### yolov4x-mish with new coordinate = 1
![화면 캡처 2022-08-10 135700](https://user-images.githubusercontent.com/88171531/183819168-b04f570a-a202-419b-b425-118a50bbdef4.png)

## Darknet ROS _ ZED2 node
![topic](https://user-images.githubusercontent.com/88171531/183785263-3f2ea8dc-a3db-4c4a-becf-0d84903ec886.png)
```
roscore
roslaunch zed_wrapper zed2.launch
roslaunch darknet_ros yolo_v4.launch
rostopic echo /darknet_ros/bounding_boxes
```
