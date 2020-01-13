#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import os,shutil,sys

def SplitGroundTruth(inputString):
    groundTruth = []
    groundTruth.append(inputString[0:4])
    #    groundTruth.append(StringToArray(inputString[4:11]))
    groundTruth.append(inputString[4:11])
    groundTruth.append(inputString[11:15])
    return groundTruth


##add four letters in groundtruth
if len(sys.argv) <3:
	sys.exit('require log name')

for j in range(3):
    logname = '/cv/DongSen/varifylog/channel_'+str(sys.argv[1])+'/result_' + str(j) + '_' + sys.argv[2] + '.txt'
    if not os.path.exists(logname):
        continue
    logfile = open(logname)
    results = logfile.readlines()
    TotalNum=0
    NotFind =0
    TotalResult=[]
    resetFound=False
    resultGetted=False
    for i,single_result in enumerate(results):
        if single_result.find('**************')==0:
            # resetFound=False
            resultGetted = False
            TotalNum+=1
            if i==len(results)-1:
#                print j,single_result
                NotFind+=1
            else:
                if results[i+1].find('**************')==0:
#                    print j,single_result
                    NotFind+=1
        else:
            if resultGetted:
                continue
            # if resetFound and resultGetted:
            #     continue
            # if single_result=='reset\n':
            #     resetFound=True
            #     continue
            if i==len(results)-1:
                TotalResult.append(single_result)
            else:
                # if j<2:
                #     print results[i+1]
                # if results[i+1]=='TCKU483178642G1 AAAA 0000000 0000 False\n':
                #     print results[i+1].find('AAAA 0000000 0000')
                #     print '$$$$$$$$$$$$$$$$$$$$$$$'
                # if results[i+1].find('AAAA')==0:
                #     print '*****************'
                if results[i+1].find('**************')==0 or results[i+1].find('AAAA 0000000 0000')>=0:
                    # predict = single_result.split(' ')[1:4]
                    # if predict == ['AAAA','0000000','0000']:
                    #     continue
                    if single_result.find('AAAA 0000000 0000')>=0:
                        continue
                    resultGetted=True
                    TotalResult.append(single_result)
    if j < 2:
        all_correct = 0
        correct_count=np.zeros((3),dtype=np.int32)
        not_correct = [[], [], []]
        for order, result in enumerate(TotalResult):
            groundtruth_string = result.split(' ')[0]
            if len(groundtruth_string) < 15:
                groundtruth_string += result.split(' ')[3]
            groundtruth = SplitGroundTruth(groundtruth_string)
            prediction = result.split(' ')[1:4]
            prediction = SplitGroundTruth(prediction[0] + prediction[1] + prediction[2])
            if groundtruth == prediction:
                all_correct += 1
            for i in range(len(groundtruth)):
                if groundtruth[i] == prediction[i]:
                    correct_count[i] += 1
                else:
                    if i == 1:
                        print groundtruth, prediction
                    not_correct[i].append(groundtruth_string + ' ' + prediction[0] + prediction[1] + prediction[2])
        print 'Total video Num: ', TotalNum
        print 'Not Find: ',NotFind
        print 'Total Result Num: ', len(TotalResult)
        countname = ['letter: ', 'digit: ', 'type: ']
        for i, correct in enumerate(correct_count):
            print countname[i], correct * 1.0 / len(TotalResult)
        print 'All correct: ', all_correct * 1.0 / len(TotalResult)
    else:
        correct_count = np.zeros((2),dtype=np.int32)
        all_correct = 0
        not_correct = [[], []]
        for order,result in enumerate(TotalResult):
            groundtruth_string = result.split(' ')[0]
            groundtruth = [groundtruth_string[0:2], groundtruth_string[2:]]
            result_str = result.split(' ')
            if len(result_str) < 3:
                prediction=['0',result_str[1][1:-1]]
            else:
                prediction=result_str[1:3]
                prediction[1]=prediction[1][0:-1]
            if groundtruth == prediction:
                all_correct += 1
            for i in range(len(groundtruth)):
                if groundtruth[i] == prediction[i]:
                    correct_count[i] += 1
                else:
                    if i == 1:
                        print groundtruth, prediction
                    not_correct[i].append(groundtruth_string + ' ' + prediction[0] + prediction[1])

        print 'Total video Num: ', TotalNum
        print 'Not Find: ', NotFind
        print 'Total Result Num: ', len(TotalResult)
        countname = ['LOC: ', 'NUM: ']
        for i, correct in enumerate(correct_count):
            print countname[i], correct * 1.0 / len(TotalResult)
        print 'All correct: ', all_correct * 1.0 / len(TotalResult)

# for i in range(3):
#     logname = '/cv/DongSen/varifylog/result_' + str(i) + '_' + sys.argv[1] + '.txt'
#     print logname
#     logfile = open(logname)
#     results = logfile.readlines()
#     TotalNum = len(results)
#     if TotalNum==0:
#         continue
#     if i <2:
#         final_results=[]
#         for order, result in enumerate(results):
#             prediction = result.split(' ')[1:4]
#             if prediction==['AAAA','0000000','0000']:
#                 continue
#             else:
#                 final_results.append(result)
#         results=final_results
#         correct_count = [0, 0, 0]
#         all_correct = 0
#         not_correct = [[], [], []]
#         for order, result in enumerate(results):
#             groundtruth_string = result.split(' ')[0]
#             if not order == (len(results) - 1):
#                 groundtruth_string_next = results[order + 1].split(' ')[0]
#                 if groundtruth_string_next == groundtruth_string:
#                     TotalNum -= 1
#                     continue
#
#             if len(groundtruth_string) < 15:
#                 groundtruth_string += result.split(' ')[3]
#             groundtruth = SplitGroundTruth(groundtruth_string)
#             prediction = result.split(' ')[1:4]
#             prediction = SplitGroundTruth(prediction[0] + prediction[1] + prediction[2])
#             if groundtruth == prediction:
#                 all_correct += 1
#
#             for i in range(len(groundtruth)):
#                 if groundtruth[i] == prediction[i]:
#                     correct_count[i] += 1
#                 else:
#                     if i == 1:
#                         print groundtruth, prediction
#                     not_correct[i].append(groundtruth_string + ' ' + prediction[0] + prediction[1] + prediction[2])
#
#         print 'Total video Num: ', TotalNum
#         countname = ['letter: ', 'digit: ', 'type: ']
#         for i, correct in enumerate(correct_count):
#             print countname[i], correct * 1.0 / TotalNum
#         print 'All correct: ', all_correct * 1.0 / TotalNum
#
#     else:
#         correct_count = [0, 0]
#         all_correct = 0
#         not_correct = [[], []]
#         for order, result in enumerate(results):
#             groundtruth_string = result.split(' ')[0]
#             if not order == (len(results) - 1):
#                 groundtruth_string_next = results[order + 1].split(' ')[0]
#                 if groundtruth_string_next == groundtruth_string:
#                     TotalNum -= 1
#                     continue
#             groundtruth=[groundtruth_string[0:2],groundtruth_string[2:]]
#             result_str=result.split(' ')
#             if len(result_str)<3:
#                 prediction=['0',result_str[1][1:-1]]
#             else:
#                 prediction=result_str[1:3]
#                 prediction[1]=prediction[1][0:-1]
#             if groundtruth == prediction:
#                 all_correct += 1
#             for i in range(len(groundtruth)):
#                 if groundtruth[i] == prediction[i]:
#                     correct_count[i] += 1
#                 else:
#                     if i == 1:
#                         print groundtruth, prediction
#                     not_correct[i].append(groundtruth_string + ' ' + prediction[0] + prediction[1])
#
#         print 'Total video Num: ', TotalNum
#         countname = ['LOC: ', 'NUM: ']
#         for i, correct in enumerate(correct_count):
#             print countname[i], correct * 1.0 / TotalNum
#         print 'All correct: ', all_correct * 1.0 / TotalNum
