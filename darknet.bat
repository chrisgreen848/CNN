@echo off 

cd D:\yolov4\darknet\build\Release

set datafile=Y:\2020-VesselDetection\Annotations\data\boat.data
set configfile=Y:\2020-VesselDetection\Annotations\data\boattiny.cfg
set weights=Y:\2020-VesselDetection\Annotations\weights\boattiny_best.weights
::set weights=Y:\2020-VesselDetection\Annotations\val\weights\30072020tiny\boattiny_16000.weights
set videofile=Y:\2020-VesselDetection\Annotations\videos\EO_0070.mp4
set outputvideo=Y:\2020-VesselDetection\Annotations\videos\yolotests\temp.mp4

echo %datafile%

darknet.exe detector demo %datafile% %configfile% %weights% %videofile% -out_filename %outputvideo% -dont_show

cd ../../../..

echo Process Complete
