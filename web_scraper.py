import requests, bs4

res=requests.get("http://127.0.0.1:5500/index.html")

soup=bs4.BeautifulSoup(res.text, "html.parser")

description=soup.find_all("p")

with open("book.txt", "w", encoding="utf-8") as file:
    for line in description:
        file.write(line.get_text())
    print("done")
    
