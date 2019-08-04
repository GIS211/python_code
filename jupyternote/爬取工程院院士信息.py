
#%%
import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import xlwt
import os
import time##限制访问频率

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）

#获取入口页面
all_url = 'http://www.cae.cn/cae/html/main/col53/column_53_xb6.html'
first_url = 'http://www.cae.cn' #拼接地址

num = 0

#获取页面
start_html = requests.get(all_url, headers=headers)  ##使用requests中的get方法来进行请求

#建立空数组
co_url = []
nam_li = []

#beautifulsoup解析网页
Soup = BeautifulSoup(start_html.text, 'lxml') ##使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）

 ##使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）

#获取所有院士名字
name_list = Soup.find('div',class_='right_md_ysmd').find_all('a')

#print(name_list)
for name in name_list:
    nam_li.append(name.get_text())
    
#print(nam_li)
#获取院士详细内容页
url_list = Soup.find('div',class_='right_md_ysmd').find_all('a')
for url in url_list:
    co_url.append(first_url+url['href'])
#print(a)

#url_list = Soup.find('')
#print(url_list)


#%%
#数据写入
xls = xlwt.Workbook() 
sht1 = xls.add_sheet('Sheet1') 

for a in co_url:

#获取院士详细内容
    contx_html = requests.get(a, headers=headers)
    res_Soup = BeautifulSoup(contx_html.text, 'lxml') ##使用BeautifulSoup来解析我们获取到的网页（‘lxml’是指定的解析器 具体请参考官方文档哦）
    context_detail = res_Soup.find('div',class_='intro').find_all('p')
#    print(str(context_detail),type(str(context_detail)))
    sht1.write(num,0,str(context_detail))
    num = num+1
    sht1.write(num-1,1,str(nam_li[num-1]))
    

xls.save('./mydata.xls')
print('all done')


#%%



