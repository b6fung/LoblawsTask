#Similariy Model: this function will take in two file names and output a score

import numpy as np
import cv2 as cv

#base class for the similarity, it just reads the file name using opencv
class similarityModel:
	def __init__(self, filename1, filename2):
		self.image1 = cv.imread(filename1)
		self.image2 = cv.imread(filename2)
		self.score = None

	def computeScore(self):
		pass

class histogramCompareModel(similarityModel):
	#These functions are for one of the model,
	# This does the following:
	# for each channel in the image, calculate the histogram
	# then computes the quadratic chi square distance between each channel of the same 
	# color.
	# The average of the scores for each channel are reported
	def computeScore(self):
		h1b, h1g, h1r = self.computeHistogram(self.image1)
		h2b, h2g, h2r = self.computeHistogram(self.image2)
		scoreb = self.computeChiSquared(h1b, h2b)
		scoreg = self.computeChiSquared(h1g, h2g)
		scorer = self.computeChiSquared(h1r, h2r)
		self.score = np.mean([scoreb, scoreg, scorer])
		return self.score

	@staticmethod
	def computeHistogram(image):
		planes = cv.split(image)
		b_hist = cv.calcHist(planes, [0], None, [256], (0,256), accumulate=False)
		g_hist = cv.calcHist(planes, [1], None, [256], (0,256), accumulate=False)
		r_hist = cv.calcHist(planes, [2], None, [256], (0,256), accumulate=False)
		cv.normalize(b_hist, b_hist, norm_type=cv.NORM_MINMAX)
		cv.normalize(g_hist, g_hist, norm_type=cv.NORM_MINMAX)
		cv.normalize(r_hist, r_hist, norm_type=cv.NORM_MINMAX)
		return b_hist, g_hist, r_hist

	@staticmethod
	def computeChiSquared(hist1, hist2):
		h1 = np.array(hist1)
		h2 = np.array(hist2)
		return 0.5*sum(np.divide(np.square(h1 -  h2),h1+h2,dtype=float, where=h1+h2!=0))

