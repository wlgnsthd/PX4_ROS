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
