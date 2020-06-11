# GOTURN

- Download [pretrained model](https://www.dropbox.com/sh/77frbrkmf9ojfm6/AACgY7-wSfj-LIyYcOgUSZ0Ua?dl=0) files in the same directory as the python file to run.
- Place the test video to perform tracking on in the same folder as the python file.
- The code requires opencv-contrib in order to run and for Jetson Nano this is a little tricky. Follow the following instructions to get the correct opencv version and packages:

```
sudo apt-get install zram-config
sudo gedit /usr/bin/init-zram-swapping
```
In the file that opens replace the line:
```
mem=$(((totalmem / 2 / ${NRDEVICES}) * 1024))
```
with (this will create a swap file of 4GB):
```
mem=$(((totalmem / ${NRDEVICES}) * 1024))
```
Updating the packages:
```
sudo apt update
sudo apt install -y build-essential cmake git libgtk2.0-dev pkg-config  libswscale-dev libtbb2 libtbb-dev
sudo apt install -y python-dev python3-dev python-numpy python3-numpy
sudo apt install -y curl
```

Install video & image formats:
```
sudo apt install -y  libjpeg-dev libpng-dev libtiff-dev libjasper-dev 
sudo apt install -y libavcodec-dev libavformat-dev
sudo apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt install -y libv4l-dev v4l-utils qv4l2 v4l2ucp libdc1394-22-dev
```

Download OpenCV Modules:
```
curl -L https://github.com/opencv/opencv/archive/4.1.0.zip -o opencv-4.1.0.zip
curl -L https://github.com/opencv/opencv_contrib/archive/4.1.0.zip -o opencv_contrib-4.1.0.zip

unzip opencv-4.1.0.zip 
unzip opencv_contrib-4.1.0.zip 
cd opencv-4.1.0/
```

Create directory:
```
mkdir release
cd release/
```

Build Opencv using Cmake:
```
cmake     -D WITH_CUDA=ON \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.1.0/modules \
        -D WITH_GSTREAMER=ON \
        -D WITH_LIBV4L=ON \
        -D BUILD_opencv_python2=ON \
        -D BUILD_opencv_python3=ON \
        -D BUILD_TESTS=OFF \
        -D BUILD_PERF_TESTS=OFF \
        -D BUILD_EXAMPLES=OFF \
        -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local ..
```
Compile the packages:
```
make -j4
sudo make install
```

- Now the important requirements are installed and the code can be run.
