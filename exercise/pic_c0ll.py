# _*_ coding:utf-8 _*_
import requests
import json
# import os
from selenium import webdriver
from lxml import etree

query = '王祖贤'  # name

''' 创建存放路径'''
# picpath = "D:\qzy_pic"
# if not os.path.isdir(picpath):
#     os.mkdir(picpath)

''' download pic '''
def download(src, name):
    dir ='./' + str(id) + '.jpg'
    dir ='./' + name + '.jpg'
    try:
        pic = requests.get(src , timeout = 10)
        fp = open(dir,'wb')   # 以二进制写方式打开文件dir
        fp.write(pic.content)
        fp.close()

    except requests.exceptions.ConnectionError:
        print('图片无法下载')

''' for 循环 请求全部的url '''
# for i in range(0, 20, 20):
#     url = 'http://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
#     html = requests.get(url).text     #得到返回结果
#     # print(html)
#     response = json.loads(html, encoding='utf-8')   #将json格式转化为python对象
#     # print(response)
#     for image in response['images']:
#         print(image['src'])  #查看当前下载的图片地址
#         # print(image['id'])
#         download(image['src'] , image['id'])  #下载一张图片

''' xpath '''
driver = webdriver.Chrome("D:\chromedriver.exe")
request_url = 'https://movie.douban.com/subject_search?search_text=' + query +'&cat=1002'
driver.get(request_url)
html = etree.HTML(driver.page_source)

src_path = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
title_path = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
srcs = html.xpath(src_path)
titles = html.xpath(title_path)
for src, title in zip(srcs,titles):
    download(src, title.text)