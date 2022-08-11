## Darknet ros rviz에서 detection image 토픽 오류
![image](https://user-images.githubusercontent.com/88171531/184043008-29af9afe-aa8b-41fd-87d1-152b6da27a92.png)
![image](https://user-images.githubusercontent.com/88171531/184043059-2dca79d0-8276-40f3-b779-b82befcd60d1.png)

```
if (viewImage_) {
    generate_image(buff_[(buffIndex_ + 1)%3], ipl_);      // 추가한 부분
    displayInThread(0);
} else {
    generate_image(buff_[(buffIndex_ + 1)%3], ipl_);
}
```
##### 다시 catkin_make
![스크린샷, 2022-08-11 09-17-59](https://user-images.githubusercontent.com/88171531/184044565-1703da95-4653-49f6-98d1-60f001f9b244.png)
### 소스코드 참고
https://github.com/IntelligentRoboticsLabs/gb_visual_detection_3d/tree/melodic
##### msgs 깃 클론
###### melodic branch 만 클론하기
```
git clone -b melodic --single-branch ~.git
```
##### catkin make 시 msgs/boundingboxes.h 문제-> msgs만 먼저 catkin_make 해주기
![화면 캡처 2022-08-11 160532](https://user-images.githubusercontent.com/88171531/184080865-a32ad1d0-242c-495f-b9ef-d9c6ef5e2e87.png)

```
catkin_make --only-pkg-with-deps darknet_ros_msgs
## 모든 것 catkin_make
catkin_make -DCATKIN_WHITELIST_PACKAGES=""
```
##### catkin_make 완료
##### darknet_3d.yaml point cloud topic && darknet_ros_3d.launch 파일 camera, yolo yaml 변경

## scaled yolov4 model ( tiny custom, csp, x-mish ) 
##### 활성화함수 mish를 어떻게 다루는 지에 따라 달라짐
### 학습시 csp와  xmish는 Loss가 줄어들지 않는 경향을 보임, 더 많이 학습해야할듯 24000 bathces 
![tiny-custom_csp_x-mish_8000](https://user-images.githubusercontent.com/88171531/184072095-20d685cf-70ea-4942-8bbc-6cc9ff438cab.png)
![tiny-custom_csp_x-mish_8000_graph](https://user-images.githubusercontent.com/88171531/184072097-2d15b343-e9f9-4fd0-8afd-189c9ac590a3.png)
