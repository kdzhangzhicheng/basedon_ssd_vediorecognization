import cv2

img_root = 'C://test2//'#这里写你的文件夹路径，比如：/home/youname/data/img/,注意最后一个文件夹要有斜杠
fps = 18    #保存视频的FPS，可以适当调整
size=(880,500)
#可以用(*'DVIX')或(*'X264'),如果都不行先装ffmepg: sudo apt-get install ffmepg
fourcc = cv2.VideoWriter_fourcc(*'XVID')
videoWriter = cv2.VideoWriter('C://test2//compose.mp4',fourcc,fps,size)#最后一个是保存图片的尺寸


for i in range(1,476):
    frame = cv2.imread(img_root+str(i)+'.jpg')
    videoWriter.write(frame)
videoWriter.release()
