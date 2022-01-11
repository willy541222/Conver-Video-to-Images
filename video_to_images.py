import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="Path to the image file.")
ap.add_argument("-s", "--step", default=30, help= "Interval of saving frames.")
ap.add_argument("-i", "--index", default=1 ,help="The initial index of saving image name.")
ap.add_argument("-o", "--save", default="./" ,help="The file path to save images.")
args = vars(ap.parse_args())

interval = args["step"] # 保存時的幀數間隔
index = args["index"] # 圖片檔名排序
frame_count = 0 # 保存時的索引
frame_index = 0 # 原影片的幀索引
savepath = args["save"] # 保存圖片的路徑

# 獲取要讀取的影片名單
filePath = args["path"]
allfilelist = os.listdir(filePath)



for videofile in allfilelist:
    raw = cv2.VideoCapture(filePath + videofile)

    if raw.isOpened():
        success = True
        print("Converting the video {} to images ... ".format(videofile))
    else:
        success = False
        print("Video Capture Failed !")

    while(success):
        success, frame = raw.read()
        if success is False:
            print("第{}讀取失敗".format(frame_index))
        
        elif frame_index % interval == 0:
            cv2.imwrite('{}{}.jpg'.format(savepath,index), frame)
            index += 1
        frame_index += 1
