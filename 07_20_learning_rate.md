# Yolov4 Training
### Laddertruck ( 2classes)
![화면 캡처 2022-07-20 104655](https://user-images.githubusercontent.com/88171531/179894812-773ee8a3-f195-4855-aae3-88e2091d967b.png)
#### Modify learning rate in .cfg 
![화면 캡처 2022-07-20 130818](https://user-images.githubusercontent.com/88171531/179894818-82227ca1-aac0-4835-b1e8-1116b4f6a18f.png)
![화면 캡처 2022-07-20 131149](https://user-images.githubusercontent.com/88171531/179895245-b4b6c519-6d7a-47cb-b934-cc9d225e80bf.png)
##### modified learning rate = 0.00261 / 8 = 0.000326
#### 어느정도 개선 되지만 여전히 Nan 생김
![화면 캡처 2022-07-20 134132](https://user-images.githubusercontent.com/88171531/179898506-ca3617b5-f3d3-4e23-9afd-7306a9b22592.png)
![화면 캡처 2022-07-20 134146](https://user-images.githubusercontent.com/88171531/179898511-875d144b-fe42-407e-97ff-952932093142.png)
##### modified learning rate =0.000163
![1](https://user-images.githubusercontent.com/88171531/179906023-3f82d9d8-a66d-4bcd-8d85-fd070fb4adc4.png)
![2](https://user-images.githubusercontent.com/88171531/179906031-39083435-5afe-44f9-b6d3-35acef81499e.png)
![3](https://user-images.githubusercontent.com/88171531/179906038-e35410e8-d285-4933-a389-260a48fd4863.png)
#### 실제 lr과 cfg lr의 관계 : 8배(?)
##### modified learning rate = 0.0000815
#### 결과
![화면 캡처 2022-07-20 160555](https://user-images.githubusercontent.com/88171531/179918741-d154c92f-d6fb-48ff-98fb-597ac7b23c12.png)
![화면 캡처 2022-07-20 160625](https://user-images.githubusercontent.com/88171531/179918748-ea6b34f1-ed69-4ed9-9086-b6daa6d02b74.png)
