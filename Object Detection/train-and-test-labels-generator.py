import os
#For performing some file operations
from bs4 import BeautifulSoup
#For reading XML files
inputs=[r"train",r"test"]
#paths to Pascal XML files of test and train datasets
outputs=["train-labels.txt","test-labels.txt"]
#The final directory in which the intermediary label files of test and train should be created
for i in range(len(inputs)):
    files=os.listdir(inputs[i])
    #Reading all files in the given directory
    files=[i for i in files if i.endswith('xml')]
    #Filtering only XML files
    #In Pascaol Voc xml format every annotated images will have an XML file whereas in COCO format all the directroy of either test or
    #train will have its respective single JSON file
    for file in files:
        with open(inputs[i]+'\\'+file,'r') as file_in:
            data=file_in.read()
            #Reading every XML file
        soup=BeautifulSoup(data,'xml')
        filename=soup.find('filename')
        filename=filename.text
        filename=filename.split(".")[0]
        #Extracting the file name and removing the extension of the file name
        objects=soup.find_all('object')
        count=len(objects)
        #Finding total number of objects annotated in the respective image
        with open(outputs[i],'a') as file_out:
            for j in range(count):
                file_out.write(filename+"\n")
                #printing the file name in the output file with respect to every object that was annotated
    print("="*25 + "Done" + "="*25)
    
