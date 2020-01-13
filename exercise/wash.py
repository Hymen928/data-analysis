# _*_ coding:utf-8 _*_
#1.完整性：利用pandas库清洗数据
import pandas as pd

# #利用平均值填充确实数据
# df['Age'].fillna(df['Age'].mean(), inplace=True)

# #利用最高频次数值填充
# age_maxf = train_deatures['Age'].value_counts().index[0]
# train_features['Age'].fillna(age_maxf, inplace=True)

# #删除空行
# df.dropna(how='all',inplace=True)

# #2.全面性：单位统一 将lbs(磅)转化为kgs(千克)
# rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
# print df[rows_with_lbs]
# for i, lbs_row in df[rows_with_lbs].iterrows():
#     #截取从头开始到倒数第三个字符之前，即去掉lbs
#     weight = int(float(lbs_row['weight'][:-3])/2.2)
#     df.at[i,'weight'] = '{}kgs'.format(weight)

# #3.合理性：非ASCII字符，删除方法
# df['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True))

# #4.唯一性：一列有多个参数
# #切分名字，删除源数据列
# df[['first_name','last_name']] = df['name'].str.split(expand=True) 
# df.drop('name', axis=1, inplace=True)

# #重复数据
# df.drop_duplicates(['first_name','last_name'],inplace=True)


# d1 = {'food':[bacon,pulled pork,bacon,Pastrami,corned beef,Bacon, pastrami, honey ham , nova lox],'English':[4.0, 3.0, NaN, 6.0, 7.5, 8.0, -3.0, 5.0, 6.0],'Math':[pig, pig, pig ,cow, cow, pig, cow, pig, cow, pig, salmon]}
#导入数据并显示
d1 = pd.read_csv("foodInformation.csv")
df = d1[:9]
print(df)
#完整性
df['ounces'] = df['ounces'].fillna(df['ounces'].mean(), inplace=True)
#全面性，统一大小写
df['food'] = df['food'].str.lower()
#合理性，删除负值
df['ounces']  = df['ounces'].apply(lambda a :abs(a))
#重复值
df.drop_duplicates(['food'],inplace=True)
print(df)