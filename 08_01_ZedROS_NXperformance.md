## Zed camera with darknet ros in Ubuntu 18.04 Melodic Cuda 11.4
https://www.stereolabs.com/docs/ros/
### Download Zed SDK
https://www.stereolabs.com/docs/installation/linux/
### Tutorial 
#### !Error
```
/usr/local/zed/samples/tutorials/tutorial 6 - object detection/python$ python3 object_detection.py 
Traceback (most recent call last):
  File "object_detection.py", line 22, in <module>
    import cv2
ImportError: libopencv_intensity_transform.so.4.4: cannot open shared object file: No such file or directory
```
#### OpenCV 자체가 ROS Melodic 설치할때 설치되었으므로 ROS내에서 구동하는 것으로 넘어감
#### catkin_make 할때 호환성을 위해 source bashrc & build & devel 폴더 삭제
#### source ./devel/setup.bash
### Zed Node 실행
```
roscore
roslaunch zed_wrapper zed2.launch
```
#### Zed ros example download
~~~
cd ~/catkin_ws/src
git clone https://github.com/stereolabs/zed-ros-examples.git
cd ../
rosdep install --from-paths src --ignore-src -r -y
catkin_make -DCMAKE_BUILD_TYPE=Release
source ./devel/setup.bash
~~~
### Displaying ZED data
```
roslaunch zed_display_rviz display_zed2.launch
```
![스크린샷, 2022-08-01 15-25-44](https://user-images.githubusercontent.com/88171531/182088137-5ad26d41-90c7-441c-b609-8517e94e39cf.png)


https://user-images.githubusercontent.com/88171531/182087979-1483baf3-50e7-4167-b6cd-6e2dd79a0d16.mp4



<details>
  <summary>rostopic list</summary>
<p>

  $ rostopic list
/clicked_point
/diagnostics
/initialpose
/move_base_simple/goal
/rosout
/rosout_agg
/tf
/tf_static
/zed2/joint_states
/zed2/zed_node/atm_press
/zed2/zed_node/confidence/confidence_map
/zed2/zed_node/depth/camera_info
/zed2/zed_node/depth/depth_registered
/zed2/zed_node/depth/depth_registered/compressed
/zed2/zed_node/depth/depth_registered/compressed/parameter_descriptions
/zed2/zed_node/depth/depth_registered/compressed/parameter_updates
/zed2/zed_node/depth/depth_registered/compressedDepth
/zed2/zed_node/depth/depth_registered/compressedDepth/parameter_descriptions
/zed2/zed_node/depth/depth_registered/compressedDepth/parameter_updates
/zed2/zed_node/depth/depth_registered/theora
/zed2/zed_node/depth/depth_registered/theora/parameter_descriptions
/zed2/zed_node/depth/depth_registered/theora/parameter_updates
/zed2/zed_node/disparity/disparity_image
/zed2/zed_node/imu/data
/zed2/zed_node/imu/data_raw
/zed2/zed_node/imu/mag
/zed2/zed_node/left/camera_info
/zed2/zed_node/left/image_rect_color
/zed2/zed_node/left/image_rect_color/compressed
/zed2/zed_node/left/image_rect_color/compressed/parameter_descriptions
/zed2/zed_node/left/image_rect_color/compressed/parameter_updates
/zed2/zed_node/left/image_rect_color/compressedDepth
/zed2/zed_node/left/image_rect_color/compressedDepth/parameter_descriptions
/zed2/zed_node/left/image_rect_color/compressedDepth/parameter_updates
/zed2/zed_node/left/image_rect_color/theora
/zed2/zed_node/left/image_rect_color/theora/parameter_descriptions
/zed2/zed_node/left/image_rect_color/theora/parameter_updates
/zed2/zed_node/left/image_rect_gray
/zed2/zed_node/left/image_rect_gray/compressed
/zed2/zed_node/left/image_rect_gray/compressed/parameter_descriptions
/zed2/zed_node/left/image_rect_gray/compressed/parameter_updates
/zed2/zed_node/left/image_rect_gray/compressedDepth
/zed2/zed_node/left/image_rect_gray/compressedDepth/parameter_descriptions
/zed2/zed_node/left/image_rect_gray/compressedDepth/parameter_updates
/zed2/zed_node/left/image_rect_gray/theora
/zed2/zed_node/left/image_rect_gray/theora/parameter_descriptions
/zed2/zed_node/left/image_rect_gray/theora/parameter_updates
/zed2/zed_node/left_cam_imu_transform
/zed2/zed_node/left_raw/camera_info
/zed2/zed_node/left_raw/image_raw_color
/zed2/zed_node/left_raw/image_raw_color/compressed
/zed2/zed_node/left_raw/image_raw_color/compressed/parameter_descriptions
/zed2/zed_node/left_raw/image_raw_color/compressed/parameter_updates
/zed2/zed_node/left_raw/image_raw_color/compressedDepth
/zed2/zed_node/left_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed2/zed_node/left_raw/image_raw_color/compressedDepth/parameter_updates
/zed2/zed_node/left_raw/image_raw_color/theora
/zed2/zed_node/left_raw/image_raw_color/theora/parameter_descriptions
/zed2/zed_node/left_raw/image_raw_color/theora/parameter_updates
/zed2/zed_node/left_raw/image_raw_gray
/zed2/zed_node/left_raw/image_raw_gray/compressed
/zed2/zed_node/left_raw/image_raw_gray/compressed/parameter_descriptions
/zed2/zed_node/left_raw/image_raw_gray/compressed/parameter_updates
/zed2/zed_node/left_raw/image_raw_gray/compressedDepth
/zed2/zed_node/left_raw/image_raw_gray/compressedDepth/parameter_descriptions
/zed2/zed_node/left_raw/image_raw_gray/compressedDepth/parameter_updates
/zed2/zed_node/left_raw/image_raw_gray/theora
/zed2/zed_node/left_raw/image_raw_gray/theora/parameter_descriptions
/zed2/zed_node/left_raw/image_raw_gray/theora/parameter_updates
/zed2/zed_node/mapping/fused_cloud
/zed2/zed_node/obj_det/objects
/zed2/zed_node/odom
/zed2/zed_node/parameter_descriptions
/zed2/zed_node/parameter_updates
/zed2/zed_node/path_map
/zed2/zed_node/path_odom
/zed2/zed_node/plane
/zed2/zed_node/plane_marker
/zed2/zed_node/plane_marker_array
/zed2/zed_node/point_cloud/cloud_registered
/zed2/zed_node/pose
/zed2/zed_node/pose_with_covariance
/zed2/zed_node/rgb/camera_info
/zed2/zed_node/rgb/image_rect_color
/zed2/zed_node/rgb/image_rect_color/compressed
/zed2/zed_node/rgb/image_rect_color/compressed/parameter_descriptions
/zed2/zed_node/rgb/image_rect_color/compressed/parameter_updates
/zed2/zed_node/rgb/image_rect_color/compressedDepth
/zed2/zed_node/rgb/image_rect_color/compressedDepth/parameter_descriptions
/zed2/zed_node/rgb/image_rect_color/compressedDepth/parameter_updates
/zed2/zed_node/rgb/image_rect_color/theora
/zed2/zed_node/rgb/image_rect_color/theora/parameter_descriptions
/zed2/zed_node/rgb/image_rect_color/theora/parameter_updates
/zed2/zed_node/rgb/image_rect_gray
/zed2/zed_node/rgb/image_rect_gray/compressed
/zed2/zed_node/rgb/image_rect_gray/compressed/parameter_descriptions
/zed2/zed_node/rgb/image_rect_gray/compressed/parameter_updates
/zed2/zed_node/rgb/image_rect_gray/compressedDepth
/zed2/zed_node/rgb/image_rect_gray/compressedDepth/parameter_descriptions
/zed2/zed_node/rgb/image_rect_gray/compressedDepth/parameter_updates
/zed2/zed_node/rgb/image_rect_gray/theora
/zed2/zed_node/rgb/image_rect_gray/theora/parameter_descriptions
/zed2/zed_node/rgb/image_rect_gray/theora/parameter_updates
/zed2/zed_node/rgb_raw/camera_info
/zed2/zed_node/rgb_raw/image_raw_color
/zed2/zed_node/rgb_raw/image_raw_color/compressed
/zed2/zed_node/rgb_raw/image_raw_color/compressed/parameter_descriptions
/zed2/zed_node/rgb_raw/image_raw_color/compressed/parameter_updates
/zed2/zed_node/rgb_raw/image_raw_color/compressedDepth
/zed2/zed_node/rgb_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed2/zed_node/rgb_raw/image_raw_color/compressedDepth/parameter_updates
/zed2/zed_node/rgb_raw/image_raw_color/theora
/zed2/zed_node/rgb_raw/image_raw_color/theora/parameter_descriptions
/zed2/zed_node/rgb_raw/image_raw_color/theora/parameter_updates
/zed2/zed_node/rgb_raw/image_raw_gray
/zed2/zed_node/rgb_raw/image_raw_gray/compressed
/zed2/zed_node/rgb_raw/image_raw_gray/compressed/parameter_descriptions
/zed2/zed_node/rgb_raw/image_raw_gray/compressed/parameter_updates
/zed2/zed_node/rgb_raw/image_raw_gray/compressedDepth
/zed2/zed_node/rgb_raw/image_raw_gray/compressedDepth/parameter_descriptions
/zed2/zed_node/rgb_raw/image_raw_gray/compressedDepth/parameter_updates
/zed2/zed_node/rgb_raw/image_raw_gray/theora
/zed2/zed_node/rgb_raw/image_raw_gray/theora/parameter_descriptions
/zed2/zed_node/rgb_raw/image_raw_gray/theora/parameter_updates
/zed2/zed_node/right/camera_info
/zed2/zed_node/right/image_rect_color
/zed2/zed_node/right/image_rect_color/compressed
/zed2/zed_node/right/image_rect_color/compressed/parameter_descriptions
/zed2/zed_node/right/image_rect_color/compressed/parameter_updates
/zed2/zed_node/right/image_rect_color/compressedDepth
/zed2/zed_node/right/image_rect_color/compressedDepth/parameter_descriptions
/zed2/zed_node/right/image_rect_color/compressedDepth/parameter_updates
/zed2/zed_node/right/image_rect_color/theora
/zed2/zed_node/right/image_rect_color/theora/parameter_descriptions
/zed2/zed_node/right/image_rect_color/theora/parameter_updates
/zed2/zed_node/right/image_rect_gray
/zed2/zed_node/right/image_rect_gray/compressed
/zed2/zed_node/right/image_rect_gray/compressed/parameter_descriptions
/zed2/zed_node/right/image_rect_gray/compressed/parameter_updates
/zed2/zed_node/right/image_rect_gray/compressedDepth
/zed2/zed_node/right/image_rect_gray/compressedDepth/parameter_descriptions
/zed2/zed_node/right/image_rect_gray/compressedDepth/parameter_updates
/zed2/zed_node/right/image_rect_gray/theora
/zed2/zed_node/right/image_rect_gray/theora/parameter_descriptions
/zed2/zed_node/right/image_rect_gray/theora/parameter_updates
/zed2/zed_node/right_raw/camera_info
/zed2/zed_node/right_raw/image_raw_color
/zed2/zed_node/right_raw/image_raw_color/compressed
/zed2/zed_node/right_raw/image_raw_color/compressed/parameter_descriptions
/zed2/zed_node/right_raw/image_raw_color/compressed/parameter_updates
/zed2/zed_node/right_raw/image_raw_color/compressedDepth
/zed2/zed_node/right_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed2/zed_node/right_raw/image_raw_color/compressedDepth/parameter_updates
/zed2/zed_node/right_raw/image_raw_color/theora
/zed2/zed_node/right_raw/image_raw_color/theora/parameter_descriptions
/zed2/zed_node/right_raw/image_raw_color/theora/parameter_updates
/zed2/zed_node/right_raw/image_raw_gray
/zed2/zed_node/right_raw/image_raw_gray/compressed
/zed2/zed_node/right_raw/image_raw_gray/compressed/parameter_descriptions
/zed2/zed_node/right_raw/image_raw_gray/compressed/parameter_updates
/zed2/zed_node/right_raw/image_raw_gray/compressedDepth
/zed2/zed_node/right_raw/image_raw_gray/compressedDepth/parameter_descriptions
/zed2/zed_node/right_raw/image_raw_gray/compressedDepth/parameter_updates
/zed2/zed_node/right_raw/image_raw_gray/theora
/zed2/zed_node/right_raw/image_raw_gray/theora/parameter_descriptions
/zed2/zed_node/right_raw/image_raw_gray/theora/parameter_updates
/zed2/zed_node/stereo/image_rect_color
/zed2/zed_node/stereo/image_rect_color/compressed
/zed2/zed_node/stereo/image_rect_color/compressed/parameter_descriptions
/zed2/zed_node/stereo/image_rect_color/compressed/parameter_updates
/zed2/zed_node/stereo/image_rect_color/compressedDepth
/zed2/zed_node/stereo/image_rect_color/compressedDepth/parameter_descriptions
/zed2/zed_node/stereo/image_rect_color/compressedDepth/parameter_updates
/zed2/zed_node/stereo/image_rect_color/theora
/zed2/zed_node/stereo/image_rect_color/theora/parameter_descriptions
/zed2/zed_node/stereo/image_rect_color/theora/parameter_updates
/zed2/zed_node/stereo_raw/image_raw_color
/zed2/zed_node/stereo_raw/image_raw_color/compressed
/zed2/zed_node/stereo_raw/image_raw_color/compressed/parameter_descriptions
/zed2/zed_node/stereo_raw/image_raw_color/compressed/parameter_updates
/zed2/zed_node/stereo_raw/image_raw_color/compressedDepth
/zed2/zed_node/stereo_raw/image_raw_color/compressedDepth/parameter_descriptions
/zed2/zed_node/stereo_raw/image_raw_color/compressedDepth/parameter_updates
/zed2/zed_node/stereo_raw/image_raw_color/theora
/zed2/zed_node/stereo_raw/image_raw_color/theora/parameter_descriptions
/zed2/zed_node/stereo_raw/image_raw_color/theora/parameter_updates
/zed2/zed_node/temperature/imu
/zed2/zed_node/temperature/left
/zed2/zed_node/temperature/right
</p>
</details>


#### ros yaml 파일 topic 수정 
##### /zed2/zed_node/left/image_rect_color 
https://user-images.githubusercontent.com/88171531/182095063-3facc7bc-8303-4e3f-aa9a-398f1d0026f8.mp4

![스크린샷, 2022-08-01 16-21-37](https://user-images.githubusercontent.com/88171531/182095056-9d00fad1-80f9-412a-bef3-5f0194308ff0.png)



______
## YOLO Darknet Jetson Xavier NX performance
![화면 캡처 2022-08-01 112542](https://user-images.githubusercontent.com/88171531/182060504-8189a68d-8294-4507-839d-2bea65214239.png)
______
## SLAM (Simultaneous Localization And Mapping)
______
## (Next) To get distance from depth
https://www.stereolabs.com/docs/tutorials/depth-sensing/
![화면 캡처 2022-08-01 173738](https://user-images.githubusercontent.com/88171531/182108558-7aaa73ea-f65c-41a7-858a-ec455f6b3a35.png)

