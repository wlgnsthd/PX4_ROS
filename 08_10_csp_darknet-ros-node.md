![화면 캡처 2022-08-10 094105](https://user-images.githubusercontent.com/88171531/183786294-81c00f4b-76c4-45ce-a503-aced832469f2.png)

## CSP Training Second Try
![화면 캡처 2022-08-10 093437](https://user-images.githubusercontent.com/88171531/183785162-f388cfbd-279d-4579-b7d3-7d9091b4cfb2.png)
https://github.com/WongKinYiu/ScaledYOLOv4/issues/13
##### yolov4x-mish.cfg 사용하거나 new coordinate = 0 적용하여 학습
##### 1) yolov4x-mish with new coordinate = 1
![화면 캡처 2022-08-10 135700](https://user-images.githubusercontent.com/88171531/183819168-b04f570a-a202-419b-b425-118a50bbdef4.png)
##### 2) yolov4x-mish with new coordinate = 0
![화면 캡처 2022-08-10 135700](https://user-images.githubusercontent.com/88171531/183821234-782c7d9a-fe70-4bf3-93f7-1feee16ee7f9.png)
###### stopped
## Darknet ROS _ ZED2 node
![topic](https://user-images.githubusercontent.com/88171531/183785263-3f2ea8dc-a3db-4c4a-becf-0d84903ec886.png)
```
roscore
roslaunch zed_wrapper zed2.launch
roslaunch darknet_ros yolo_v4.launch
rostopic echo /darknet_ros/bounding_boxes
```
## darknet_ros_zed 소스코드 사용
https://github.com/leoll2/darknet_ros_zed
##### error (maybe opencv version problem)
![스크린샷, 2022-08-10 15-46-40](https://user-images.githubusercontent.com/88171531/183835111-18ffeabe-1a1f-4aa2-8eb9-5fc4e186b076.png)
##### cpp 다른 내용 수정
```
static float get_pixel(image m, int x, int y, int c)
{
    assert(x < m.w && y < m.h && c < m.c);
    return m.data[c*m.h*m.w + y*m.w + x];
}

namespace darknet_ros {

char *cfg;
char *weights;
char *data;
char **detectionNames;
sem_t sem_new_image_; // Semaphore to indicate new image

YoloObjectDetector::YoloObjectDetector(ros::NodeHandle nh)
    : nodeHandle_(nh),
      imageTransport_(nodeHandle_),
      numClasses_(0),
      classLabels_(0),
      rosBoxes_(0),
      rosBoxCounter_(0),
      imgSync_(ApproxTimePolicy(3), imageSubscriber_, dmapSubscriber_)
{
  ROS_INFO("[YoloObjectDetector] Node started.");

```
```
void YoloObjectDetector::zedCameraCallback(const sensor_msgs::ImageConstPtr& img_msg,
                                           const sensor_msgs::ImageConstPtr& dmap_msg)
{
  ROS_DEBUG("[YoloObjectDetector] USB image received.");

  cv_bridge::CvImagePtr cam_image, cam_dmap;

  try {
    cam_image = cv_bridge::toCvCopy(img_msg, sensor_msgs::image_encodings::BGR8);
    cam_dmap = cv_bridge::toCvCopy(dmap_msg, sensor_msgs::image_encodings::TYPE_32FC1);
  } catch (cv_bridge::Exception& e) {
    ROS_ERROR("cv_bridge exception: %s", e.what());
    return;
  }

  if (cam_image && cam_dmap) {
    {
      boost::unique_lock<boost::shared_mutex> lockImageCallback(mutexImageCallback_);
      imageHeader_ = img_msg->header;
      camImageCopy_ = cam_image->image.clone();
      camDmapCopy_ = cam_dmap->image.clone();
    }
    {
      boost::unique_lock<boost::shared_mutex> lockImageStatus(mutexImageStatus_);
      imageStatus_ = true;
    }
    frameWidth_ = cam_image->image.size().width;
    frameHeight_ = cam_image->image.size().height;
    sem_post(&sem_new_image_);
  }
  return;
}
```

```
float YoloObjectDetector::getObjDepth(float xmin, float xmax, float ymin, float ymax)
{
  /* Given the bounding box, read the depth from 9 internal points. Sort them, then take the second minimum.
   * This is possibly better than taking the minimum as it may be a spurious outlier, for some reason. */
  std::vector<float> depths;
  float x, y, d;
  int refs = 3;
  
  for (int i=1; i < refs+1; ++i) {
    for (int j=1; j < refs+1; ++j) {
      x = xmin + j*(xmax-xmin)/(refs+1);
      y = ymin + i*(ymax-ymin)/(refs+1);
      d = camDmapCopy_.at<float>((int)(y*frameHeight_), (int)(x*frameWidth_));
      if (std::isnormal(d))
        depths.push_back(d);
    }
  }
  
  std::sort(depths.begin(), depths.end());

  if (depths.size() > 1) {
    // printf("depth at (%d, %d): %f\n", (int)((xmin+xmax)/2*frameWidth_), (int)((ymin+ymax)/2*frameHeight_), depths[1]);
    return depths[1];
  } else if (depths.size() == 1) {
    // printf("depth at (%d, %d): %f\n", (int)((xmin+xmax)/2*frameWidth_), (int)((ymin+ymax)/2*frameHeight_), depths[0]);
    return depths[0];
  } else return NAN; 
}
```
