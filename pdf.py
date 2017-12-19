#!/usr/bin/env python
#coding:utf-8
import requests
import os

url = "http://pdfs.semanticscholar.org/bfee/e8cbb8eaa7d8fe53eaa14f57aa1efa32ed2d.pdf"
root = "G://PDF//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")