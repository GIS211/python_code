
#%%
import re
import pandas as pd
#from pandas import DataFrame,Series


#%%
data_source = pd.read_excel('小区列表.xlsx')

data_source.head()

data_source.name.tolist


#%%
import requests
from bs4 import BeautifulSoup


#%%
url_search = 'https://km.fang.anjuke.com/loupan/s?kw='
#type(data_source.columns)

kw = {'kw':'融城昆明湖'}

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
response = requests.get("https://km.fang.anjuke.com/loupan/s?",params = kw, headers = headers)

# 查看响应码
print(response.status_code)


#查看响应页面内容
#print(response.text )

html_text = response.text 
soup = BeautifulSoup(html_text,"html.parser")


#%%
find_url = soup.find_all('a',class_ = 'lp-name')

#print(find_url[0])
final_url = find_url[0].get('href')

print(final_url)


#%%
response = requests.get(final_url,headers = headers)

# 查看响应码
print(response.status_code)

#查看响应页面内容
#print(response.text )

html_text = response.text 
soup = BeautifulSoup(html_text,"html.parser")
print(html_text)


#%%
find_url2 = soup.find_all('a',class_ = 'lpAddr-text g-overflow')

string_ = str(find_url2[0])
print(string_)

m = re.findall(r'>(.*?)<', string_)


#%%
print(m)
data_source.loc_desc[1]


#%%



#%%
for loupan in data_source.name:
    print(loupan)


#%%



