[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fwlgnsthd%2FPX4_ROS&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
# Jetson Xavier AGX
``` 
Jetpack 4.6.2
Cuda 10.2
OpenCV 4.1->3.4
ROS-melodic
darknet-ROS
```
# Version Check
```
# JetPack & CUDA
git clone https://github.com/jetsonhacks/jetsonUtilities
cd jetsonUtilities
python jetsonInfo.py
# OpenCV
pkg-config --modversion opencv
pkg-config --modversion opencv3
pkg-config --modversion opencv4

```
![Screenshot from 2022-07-06 16-08-53](https://user-images.githubusercontent.com/88171531/177490683-f1070dad-716c-449c-af0e-d1aae0ade746.png)

## Jtop install
```
sudo -H pip3 install -U jetson-stats
jtop
```

