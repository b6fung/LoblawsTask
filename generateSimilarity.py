import csv
import argparse
import time
from scoreModel import *

#This block of code, parses the inputs
parser = argparse.ArgumentParser(description="parse file name")
parser.add_argument("--csvfile",dest="csvFile")
parser.add_argument("--outcsvfile",dest="outCSVFile")
args = parser.parse_args()
csvFile = args.csvFile
outputCSVFile = args.outCSVFile

#Temp arrays for writing to CSV files
imageFilenamePairList = []
outputCSVList = []

#HELPER FUNCTIONS FOR READING AND WRITING CSV FILES

#Assume that the all file names can fit in memory
def readCSV (csvFile):
	with open(csvFile) as csvfile:
		reader = csv.reader(csvfile, delimiter=" ")
		for row in reader:
			imageFilenamePairList.append(row[0].split(","))

def writeCSV(destFile):
	with open(destFile, "w+") as csvfile:
		for row in outputCSVList:
			csvfile.write(','.join(row))

##MAIN DRIVER CODE
#Should do three things:
# Read the csv
# Compute the similartiy
# Write the csv

readCSV(csvFile)

for row in imageFilenamePairList:
	startTime = time.time()
	#we are using the histogram compare model for this
	model = histogramCompareModel(*row)
	score = model.computeScore()
	endTime = time.time() - startTime
	outputCSVList.append(row+[str(score)]+[str(endTime)])
	del model

writeCSV(outputCSVFile)
