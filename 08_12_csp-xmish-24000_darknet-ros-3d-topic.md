## csp x-mish 24000 max batches 수행 결과
![csp_x-mish_24000_graph](https://user-images.githubusercontent.com/88171531/184265244-f43a9c06-6373-4dc5-ba85-3d10a9d079c1.png)

![csp_x-mish_24000](https://user-images.githubusercontent.com/88171531/184265256-2bb77e2a-fb78-4fcd-b35b-80f2803c16d0.png)

##### 또한 새롭게 ema weight가 생겼는데 Exponential moving average, averaged sgd에 사용됨, 다음은 ema weight의 mAP
https://pytorch.org/blog/pytorch-1.6-now-includes-stochastic-weight-averaging/
![csp-ema_24000](https://user-images.githubusercontent.com/88171531/184265566-a61b17d8-5de9-4dc7-b35d-eaafbed5f602.png)

##### 8000batch에서 더 좋은 결과 나왔으므로, 이것에서 csp만 learning rate를 gpu 3개를 사용할때 0.000435(0.00087의 절반)로 training해본다

## v4-custom, tiny-custom, csp, x-mish darknet ros inference 결과
#### 일반 v4
![v4](https://user-images.githubusercontent.com/88171531/184270139-57fe238c-9380-4b14-98ea-e69119628e76.png)
#### v4-custom
![v4-custom](https://user-images.githubusercontent.com/88171531/184269332-e45b4827-4b91-4620-81a0-ef8b6f821beb.png)
#### tiny-custom
![v4-tiny-custom](https://user-images.githubusercontent.com/88171531/184269359-930958d7-c23d-479c-b611-10fd9f69fb33.png)
#### csp (error)
![v4-csp_fps2 5](https://user-images.githubusercontent.com/88171531/184269395-9533ecef-a245-4edb-ab39-38d5cc961b61.png)
#### x-mish (error)
![v4x-mish_fps1 3](https://user-images.githubusercontent.com/88171531/184269424-337012a6-fdf6-4128-a4e9-6d4f28c702ae.png)
##### Loss가 줄어들지 않고 mAP만 커지는 경우 이러한 오류 발생 (예상)

## darknet_ros_3d
### bounding_boxes topic
![스크린샷, 2022-08-12 11-02-36](https://user-images.githubusercontent.com/88171531/184286166-d33f6dfb-55f6-4b43-ad84-091208b6566c.png)
#### inf나 nan떠서 생기는 문제 
![스크린샷, 2022-08-12 11-20-57](https://user-images.githubusercontent.com/88171531/184286300-b47131d2-5e2d-4b73-86cd-57001ab067e4.png)

##### 너무 가까우면 거리 계산값이 너무 커짐
### Topic Analysis
