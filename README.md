# PASCAL-VOC-XML-to-COCO-Annotation-generator
The following repository will contain two python script files that helps you in converting the PASCAL VOC XML annotations to COCO annotations.

## what are PASCAL VOC XML annotations?
The annotation format originally created for the Visual Object Challenge (VOC) has become a common interchange format for object detection labels. In this format every annoatated image will have an XML file associated with it in which inforamtion of file such as filename, widht and height will be specified. Along with this information, the details about the annotated objects will also be in the XML file.

## What are COCO JSON format annotations?
COCO annotations are inspired by the Common Objects in Context (COCO) dataset. It is one of the best image datasets available, so it is widely used in cutting edge image recognition artificial intelligence research. In this format a directory of annotated images will have one JSON file that represents all the images in the directory along with the objects that are annotated in each image of the directory. Generally we use two JSON files one for Test dataset and the other for Train Dataset.

## How to use this repository to convert VOC XML annotations to COCO JSON annotations?
Step:1

Inside the directory that contatin test and train directories create a text file with the name 'labels.txt' and then enter the names of all the objects that are annotated  in the images. The name of each object should be specified in a new line.

Step:2

Run the file 'train-and-test-labels-generator.py' to get the files 'train-labels.txt' and 'test-labels.txt'. These label files are required to conver the Pascal VOC xml format of annotations to COCO format annotations. Run the file by placing it in the directory that contain train and test directories.

Step:3

This is the final step. In this step the file named 'coco-generator.py' must be executed using the command line. Copy and paste the file in the directory that contains train and test directories. Open command line and navigate to the folder that contains 'coco-generator.py' using the 'cd' command. In the command line execute the following commands each at once to get the 'train.json' and 'test.json' files.
1. ```python coco-generator.py --ann_dir test/ --ann_ids test-labels.txt --labels labels.txt --output test.json --ext xml```
2. ```python coco-generator.py --ann_dir train/ --ann_ids train-labels.txt --labels labels.txt --output train.json --ext xml```


**The files 'train.json' and 'test.json' that are obtianed in the last step are the required COCO JSON Format annotations that are obtained from PASCAL VOC XML format annotations.**
