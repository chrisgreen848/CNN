"""Simple scripts to rename a folder of images"""


dir_path = "Z:/2020-VesselDetection/Annotations/prelabelling/snaps/"

os.chdir(dir_path)
newname = "12_august_2020_"
count = 0
for file in glob.glob("*.jpg"):
    originalName = dir_path + file
    print(originalName)
    imgNo = str(count).zfill(4)
    fullnewname = dir_path + newname + imgNo + ".jpg"
    os.rename(originalName, fullnewname)
    count += 1
