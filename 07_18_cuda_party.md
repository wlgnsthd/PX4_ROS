## Custom Image Training 정리
## Mission : 4 classes로 분류해서 yolov3 yolov4 training
## Cuda 복수 버전 설치 
### AlexeyAB darknet은 Cuda 10.2이상의 버전 요구함
### sm 72나 sm 75로 시도해도 Training불가
### 10.1버전을 그대로 두고 11.0버전 설치 : 불가
### 신 버전 설치후 구 버전 설치가능
#### https://developer.nvidia.com/cuda-11.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=2004&target_type=deblocal
### runfile로 시도했으나 여러 오류발생
![화면 캡처 2022-07-27 100052](https://user-images.githubusercontent.com/88171531/181137960-b3094ca5-532f-489e-904f-ee16dd85af32.png)
### local file 다운로드 받아 11.0버전 설치
##### https://wooriel.tistory.com/53
https://velog.io/@boom109/nvidia-driver-cuda-toolkit-cudnn-install
#### vim /etc/bash.bashrc
##### 마지막 줄 아래 추가 (cuda path및 cuda library path를 지정)


```
##### ADD #####
export PATH=/usr/local/cuda-11.0/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.0/extras/CUPTI/lib64:$LD_LIBRARY_PATH
################

```
```
 source /etc/bash.bashrc
```

##### 설정 한 PATH를 현재 접속해 있는 터미널에 바로 적용 
![화면 캡처 2022-07-19 085759](https://user-images.githubusercontent.com/88171531/179636373-09b5b0e4-faec-4bdb-877d-447b3dde08e7.png)
![화면 캡처 2022-07-19 101736](https://user-images.githubusercontent.com/88171531/179643186-a434b412-e5f5-4588-961a-e1a4797dea03.png)
### 11.1 cuda 설치.. (rtx30..은 450이상 지원)
![화면 캡처 2022-07-26 153237](https://user-images.githubusercontent.com/88171531/180939148-65967e37-2084-4c75-8557-39f179322fda.png)
