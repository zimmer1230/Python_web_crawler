import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
rs = requests.session() # 建立一個 session 紀錄資訊
rs.cookies.set("over18", "1", domain="ptt.cc") # 設置 cookies 繞過檢查 18 歲
res = rs.get(url)

#把 HTML 丟進 beautiful soup 解析
soup = BeautifulSoup(res.text,
"html.parser")
# 找到我們要的資料
rEnts = soup.select('.r-ent')
# 初始化 posts 儲存我們得到的資料
posts = []
for rEnt in rEnts:
    post = {}
    nrec = rEnt.select_one('.nrec > span')
    post['date'] = rEnt.select_one('.date').text
    post['author'] = rEnt.select_one('.author').text
    post['score'] = nrec.text if nrec != None else None
    post['title'] = rEnt.select_one('.title > a').text
    post['url'] = rEnt.select_one('.title > a')["href"]
    posts.append(post)

import csv
# 寫入 CSV
keys = posts[0].keys()
with open('C:\\Users\\pao.wen\\Documents\\109-2_WFH\\python\\Python_web_crawler\\posts.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(posts)