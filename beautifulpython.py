import requests
from bs4 import BeautifulSoup
import csv

res = requests.get('http://www.hikkoshi-sakai.co.jp/company/network/')
res.encoding = res.apparent_encoding
def main():
    full_list=[]
    soup = BeautifulSoup(res.text, 'html.parser')
    t= soup.find_all("tr")
    t=str(t)
    st=t.split("</tr>")
    st.pop(0)
    for i in st:
        list=[]
        i = i.splitlines()
        if  len(i)<4:
            continue
        name = i[1].replace('<th>', '').replace('</th>', '')
        location = i[3].replace('\t', '').replace('</td>', '')
        if name == "名称":
            continue
        list.append(location)
        list.append(name)
        full_list.append(list)
    with open('sakai.csv', 'a', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in full_list:
            writer.writerow(i)
    print(full_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
