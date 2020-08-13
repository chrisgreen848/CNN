# -*- coding: utf-8 -*-
"""
Intermittant frames saved of all videos in a directory
"""



import argparse
import cv2
import os
import glob

def save_vid_to_images(filename, savedir):
   
    FPS = 60
    print("Starting Video")
    vidcap = cv2.VideoCapture(filename)
    vidcap.set(cv2.CAP_PROP_FPS, 5)
    success,image = vidcap.read()
    count = 0
    frame = 0
    saved = 0
    while success:
        name = filename.split(".")
        name = name[0] + str(count)
        name = savedir + name+".jpg"
        #print(name)
        #print("frame number ", frame)
        success,image = vidcap.read()
        if frame > FPS: 
            #print(name)             
            cv2.imwrite(name, image) # save frame as JPEG file  
            
            print('Read a new frame: ', success)
            frame = 0
            saved += 1
        count += 1
        frame+=1
    print("Video frame capturing for ",filename," Complete")
    

# command line arguement
parser = argparse.ArgumentParser(description='Plot histograms of labelled data')
parser.add_argument('--File', action='store', dest = 'filename',
                    help='Video to be split location (will be saved to the same folder as this script)')                  

args = parser.parse_args()
print("File name is : ", args.filename)
filename = args.filename
#Dir = "/Data/Flight Data/AR5 Evo/AVOCETDeployment/2020/06. JUN/01062020/Onboard Video/Video/"
Dir = "Data/Flight Data/AR5 Evo/AVOCETDeployment/2020/06. JUN/25062020/Onboard Video/"
os.chdir(Dir)
amount = 0
vidList = []
for file in glob.glob("*.mp4"):
    vidList.append(file)


newDir = "Z:/2020-VesselDetection/Annotations/prelabelling/"
    
for i in range(len(vidList)):
    filename = Dir + vidList[i]
    dirname = vidList[i].split(".")
    dirname = dirname[0]
    dirname = newDir+dirname + "/"
    print(dirname)
    os.mkdir(dirname)
    filename = Dir + vidList[i]
    print("filename is ", filename)
    save_vid_to_images(filename, dirname)   
