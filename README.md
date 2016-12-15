# html5gui-poc
Proof of concept for rover GUI in HTML5 - currently just a video streaming test

to test:
roscore
rosrun web_video_server web_video_server
rosrun vid_stream talker.py
then just open index.html in your browser - should stream your 0th webcam device to the browser
