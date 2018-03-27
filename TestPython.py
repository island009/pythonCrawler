#!/usr/bin/python
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/'
     req = requests.get(url = target)
     html = req.text
     # print(html)
     bf = BeautifulSoup(html,"lxml")
     texts = bf.find_all('div', class_ = 'listmain')
     for i in texts:
     	# text属性，提取文本内容，滤除br标签
     	# print i.text.encode('utf-8').replace('\xa0*8','\n\n')
     	print(i.encode('utf-8'))
     	pass
