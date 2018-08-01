# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:42:35 2018
To catch the TOP ranking movie in the Maoyan website
@author: moxiaodong
"""

import requests
import re
header = {
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
}
res = requests.get('http://maoyan.com/board/4',headers=header).text
#curres=res.split("\n")
p2 = '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">' + '<a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>' + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
pattern2 = re.compile(p2,re.S)
item=re.findall(pattern2,res)
for j in item:
    print (j)
