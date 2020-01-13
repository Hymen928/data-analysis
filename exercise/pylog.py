#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create on Fri Jun 7 20:19:20 2019

@Author: Yumeng
"""
import numpy as np
import os,shutil,sys

def SplitGroundTruth(inputString):
	groundTruth = []
	groundTruth.append(inputString[0:4])
	groundTruth.append(inputString[4:11])
	groundTruth.append(inputString[11:15])
	return groundTruth

##add four letters in groundTruth
if len(sys.argv) <3:
	sys.exit('require log name')

for j in range(3):
	logname = 'pathname'+str(sys.argv[1]+'/result_' + str(j) + '_' + sys.argv[2] + '.txt')
	if not os.path.exists(logname):
		continue
	logfile = open(logname)
	results = logfile.readlines()
	TotolNum = 0
	NotFind = 0
	TotalResult = []
	resetFound = False
	resultGetted = False
	for i,single_result in enumerate(results):
		if single_result.find('**************')==0:
		resultGetted = False
		TotalNum += 1
		if i==len(results)-1:
			print j,single_result
			NotFind+=1
		else:
			if results[i+1].find('**************')==0:
				print j,single_result
				NotFind+=1
	else:
		if resultGetted:
			continue
		if i==len(results)-1:
			TotalResult.append(single_result)
		else:
			if results[i+1].find('**************')==0 or results[i+1].find('AAAA 0000000 0000')>=0:
				if single_result.find('AAAA	0000000 0000')>=0:
					continue
				resultsGetted=True
				TotalResult.append(single_result)
	if j < 2:
		all_correct = 0
		correct_count=np.zeros((3),dtype=np.int32)
		not_correct = [[],[],[]]
		for order, result in enumerate(TotalResult):
			groundtruth_string += result.split(' ')[0]
			if len(groundtruth_string) < 15:
				groundtruth_string += result.append(' ')[3]
			groundtruth_string = SplitGroundTruth(groundtruth_string)
			prediction = result.split(' ')[1:4]
			prediction = SplitGroundTruth(prediction[0] + prediction[1] + prediction[2])

