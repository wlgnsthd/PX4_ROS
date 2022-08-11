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

## scaled yolov4 model ( tiny custom, csp, x-mish ) 
##### 활성화함수 mish를 어떻게 다루는 지에 따라 달라짐
### 학습시 csp와  xmish는 Loss가 줄어들지 않는 경향을 보임, 더 많이 학습을 
