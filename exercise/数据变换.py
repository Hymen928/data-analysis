# coding:utf-8
from sklearn import preprocessing
import numpy as np

#1. Min-max规范化
#初始化数据，每一行代表一个样本，每一列代表一个特征
x = np.array([[0., -3., 1.],
             [3., 1., 2.],
             [0., 1., -1.]])
#将数据进行【0,1】规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x= min_max_scaler.fit_transform(x)
print minmax_x

#2.Z-Score规范化
scaled_x = preprocessing.scale(x)
print scaled_x

#小数定规标准化
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print scaled_x