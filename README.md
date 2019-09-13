#Loblaws Image Similarity Tool
##This document is to review the tool to see how similar two images are.

###Installation: 
This application uses python to run everything so first install python [here](https://www.python.org/downloads/).  
To ready the program, open command line and ```cd``` into where you cloned this project.
####Windows
Then you need to activate the virtual envrionment, you can do that with the command ```imageSim\Scripts\activate.bat```
####Mac/Linux
You still need to activate the virtual environment, for macos or linux type in ```source imageSim/bin/activate``` in the terminal

###Usage
To use the tool, there are two files that you need  
1. First you need the csv file that has the image pairs full path  
2. A name for the destiniation csv full path  

Once you have those then use the command  
```python generateSimilarity.py --csvfile /path/to/csv --outcsvFile /path/to/output/csv```

The results will be stored in the output csv specified in the command

###Implementation Details
This program is split into two main parts  
1. ```genereateSimularity.py```: This file is the driver code in which it would read a csv, compute the differences then output a csv with the details of the csv explained below  
2. ```scoreModel.py```: This file is where you calculate the simularity of the two images ine question  

  * Currently only one model is used for speed purposes.  What is implemented is a comparison of the two image by first computing their colour histogram for each channel.  Then taking computing the distance using the chi squared measure giving a result.  The result should be 0 if they are the same and 1 if they are very different with values closer to 0 meaing they are similar.

One can extend this my adding more classes to the ```scoreModel.py``` namely using SSIM or feature extraction

To extend the ```scoreModel.py``` all that is required is to create a class extending ```similarityModel``` and implementing a ```computeScore()``` function that returns a the result of the calculation.

###CSV Details
This tool has the assumptions on the csvinput in which there are two complete path file names which represent the two image paths separated with a comma as shown

![alt text](./assets/inputcsv.png)  

with the output csv in the folloiwng for  

![alt text](./assets/outputcsv.png)
