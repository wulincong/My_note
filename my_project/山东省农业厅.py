import requests
from bs4 import BeautifulSoup
f = open("res.csv","w",encoding="gbk")
url = "http://nync.shandong.gov.cn/yysjk/spyb/lssp/"
def main(i):
    index_url = url + "index_"+str(i)+".html"
    se = requests.session()
    context = se.get(index_url, timeout=10)
    data = context.content.decode('utf8')
    soup = BeautifulSoup(data)
    data = str(soup.find("div",class_ = "sjknei").get_text())
    lis = data.split("\n")
    lis.pop(0)
    csv_write(lis,6,len(lis)//6)
def csv_write(l,j,n):
    for i in range(n):
        for x in range(j):
            f.write(l[i*j+x]+",")
        f.write("\n")
for i in range(1,50):
    main(i)
