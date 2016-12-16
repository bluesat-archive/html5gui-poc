# html5gui-poc
Proof of concept for rover GUI in HTML5 - currently just a video streaming test


to test:
roscore
rosrun web_video_server web_video_server
then either:
rosrun vid_stream video0_image.py
this one ^ I wrote, uses cvbridge, bit slow i think
or
roslaunch src/video_stream_opencv/webcam.launch
this one ^ is its own package, seems faster?

then just open index.html in your browser - should stream your 0th webcam device to the browser

