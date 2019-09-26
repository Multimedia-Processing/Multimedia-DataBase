ffmpeg -init_hw_device cuda -c:v  h264_cuvid -hwaccel cuda -i input\0725.mp4 -init_hw_device cuda -c:v h264_nvenc -b:v 4400k -ab 512k -ar 48000 -r 30 -s 720x480 -aspect 4:3 output\0725.mp4
