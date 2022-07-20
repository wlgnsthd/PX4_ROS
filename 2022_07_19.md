## Cudnn 8.4.0 설치
```
sudo tar xvf cudnn-linux-x86_64-8.4.0.27_cuda11.6-archive.tar.xz
sudo mv cudnn-linux-x86_64-8.4.0.27_cuda11.6-archive cuda
sudo cp cuda/include/cudnn* /usr/local/cuda-11.7/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-11.7/lib64
sudo chmod a+r /usr/local/cuda-11.7/include/cudnn.h /usr/local/cuda-11.7/lib64/libcudnn*

sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8.0.5 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8
sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8.0.5  /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8
sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8.0.5  /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8
sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8.0.5  /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8
sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_train.so.8.0.5  /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_train.so.8
sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8.0.5 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8
sudo ln -sf /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8.0.5  /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8

sudo ldconfig
```
#### 오류시 deb파일로 설치
##### https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html
### 설치후 darknet training 실시
#### Error
![화면 캡처 2022-07-19 111429](https://user-images.githubusercontent.com/88171531/179649513-a0241f26-f724-4acc-9312-44311b408b38.png)
#### driver 450 cuda 11.1 cudnn 8.0.5 재설치
```
nvidia-smi
nvcc -V
ldconfig -N -v $(sed 's/:/ /' <<< $LD_LIBRARY_PATH) 2>/dev/null | grep libcudnn
```


### 모두 삭제후 Cuda 11.7 Nvidia driver 515버전 설치 완료 (runfile 어찌저찌)
#### Cudnn 설치
![화면 캡처 2022-07-19 175416](https://user-images.githubusercontent.com/88171531/179709982-ba4f88c1-7592-46a5-b7be-20be0374e9ad.png)
