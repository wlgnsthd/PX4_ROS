# Training
## 탐지성능
![image](https://user-images.githubusercontent.com/88171531/180895240-7db01320-a2d9-4c7b-ab55-258c2dcff48c.png)
### 각 파라미터가 의미하는것?
## 4 class (drone, radio, large mark, small mark)
### first try (80000 batch, lr =0.0000408)
![chart_yolov4](https://user-images.githubusercontent.com/88171531/180898095-af4f3505-b157-4c33-9c11-c4bcd8fac644.png)
![Screenshot from 2022-07-26 09-33-36](https://user-images.githubusercontent.com/88171531/180898100-60ca64b2-2ea2-4e51-ba11-d9e26e20786c.png)

### ! mAP 그래프에서 나타나지 않는 문제
![화면 캡처 2022-07-26 092743](https://user-images.githubusercontent.com/88171531/180897112-2802eaba-5cbe-48b1-9611-ca9e753beab6.png)
![화면 캡처 2022-07-26 093724](https://user-images.githubusercontent.com/88171531/180897966-fdd10de3-1ec9-4331-9858-ecd03e0da3e8.png)
## second try (10000 batch, lr =0.0000408)
![chart_yolov4](https://user-images.githubusercontent.com/88171531/180921663-d97a195b-072b-4665-b822-b184d1f72e7b.png)
![Screenshot from 2022-07-26 13-07-43](https://user-images.githubusercontent.com/88171531/180921666-3a91a157-1cfa-4382-b36e-b401c01ee5f8.png)
### continue training (10000 batch, lr=same)
```
# cfg 수정후
./darknet detector train data/obj.data yolo-obj.cfg backup/yolo-obj_last.weights
```
### Result ( 6000* 4 =24000 batches -> tomorrow)
![chart_yolov4](https://user-images.githubusercontent.com/88171531/180958029-fc954c19-cbcd-4896-a828-af36d03a4e80.png)

![Screenshot from 2022-07-26 17-16-40](https://user-images.githubusercontent.com/88171531/180958944-226ac951-49b8-405d-97e7-349f89afe247.png)

### 24000 Result
![화면 캡처 2022-07-27 124325](https://user-images.githubusercontent.com/88171531/181156123-4da92f35-8de4-4e8e-aac3-302ccb1316a3.png)
![chart](https://user-images.githubusercontent.com/88171531/181156278-b723eae9-4a44-4335-aeb2-4eff7aa0b53e.png)

#### yolov4 done.
